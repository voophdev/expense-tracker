from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.services.user_service import UsersService
from myproject.services.response_service import ResponseService


class Login(APIView):
    permission_classes = [AllowAny]

    def __init__(self, service=None):
        self.response = ResponseService()
        self.service = service or UsersService()

    def post(self, request: Request):

        try:

            email = request.data.get('email')
            password = request.data.get('password')

            if not email and not password:
                return self.response.bad_request_response(
                    error_details="email and password can't be blank"
                )

            if not self.service.get_user(email=email):
                return self.response.not_found_response(
                    error_details="User not found"
                )

            user = authenticate(email=email, password=password)

            print(user)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                user_data = self.__get_user_info(
                    user, email, access_token, refresh_token)

            return self.response.ok_response(
                response_data=user_data
            )

        except Exception as e:
            return self.response.internal_error_response(e)

    def __get_user_info(self, user, email, access_token, refresh_token):

        values = [
            'id', 'username', 'first_name', 'last_name', 'email', 'address', 'mobile_number', 'is_active'
        ]

        data = self.service.get_user(email=email, values=values)

        user_data = data[0]

        all_permissions = user.get_all_permissions()
        user_groups = user.groups.all()
        user_group = ', '.join(
            group.name for group in user_groups) if user_groups else None

        return {
            "username": user_data['username'],
            "user_id": user_data['id'],
            "full_name": user_data['first_name'] + " " + user_data['last_name'],
            "first_name": user_data['first_name'],
            "last_name": user_data['last_name'],
            "address": user_data['address'],
            "mobile_number": user_data['mobile_number'],
            "email": user_data['email'],
            "token": access_token,
            "refresh_token": refresh_token,
            "is_active": user_data['is_active'],
            "user_permissions": all_permissions,
            "user_group": user_group,
        }
