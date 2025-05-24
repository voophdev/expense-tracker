from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from expense_tracker.models import Category
from expense_tracker.services.category_service import CategoryService
from expense_tracker.serializers.category_serializer import CategoryOutputSerializer, CategoryInputSerializer
from myproject.services.response_service import ResponseService as response


class CategoryViewSet(ViewSet):

    def list(self, request: Request) -> Response:
        """
        Handle GET request to retrieve categories.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: The HTTP response containing category data.
        """

        user_id = request.user.id

        try:

            category_list = CategoryService.list_categories(user_id=user_id)

            serializer = CategoryOutputSerializer(category_list, many=True)

            return response.ok(
                response_data=serializer.data
            )

        except Exception as e:
            return response.internal_error(request, e)

    def retrieve(self, request: Request, pk: int) -> Response:
        """
        Handle GET request to retrieve a specific category from a specific user.

        Args:
            request (Request): The HTTP request object.
            category_id (int): The id of the category being retrieved.

        Returns:
            Response: The HTTP response containing category data.
        """

        user_id = request.user.id

        try:

            category = CategoryService.get_category(
                category_id=pk, user_id=user_id)

            serializer = CategoryOutputSerializer(category)

            return response.ok(
                response_data=serializer.data
            )

        except Category.DoesNotExist:
            return response.not_found(
                error_details=f"No existing category with the id: {pk}"
            )

        except Exception as e:
            return response.internal_error(request, e)

    def create(self, request: Request) -> Response:
        """
        Handle POST requests to create a new category.

        Args:
            request(Request): The HTTP request object.

        Returns:
            Response: The HTTP Response containing the category created.
        """

        user_id = request.user.id

        try:

            serializer = CategoryInputSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(
                    is_default=False,
                    user_id=user_id
                )
                return response.ok(
                    response_data=serializer.data
                )

            return response.bad_request(
                error_details=serializer.errors
            )

        except Exception as e:
            return response.internal_error(request, e)

    def update(self, request: Request, pk: int):
        """
        Handles PUT requests to update an existing category for a specific user.

        Args: 
            request(Request): The HTTP request object.
            category_id(int): The id of the category that needs to be updated.

        Response: The HTTP Response containing the updated category.
        """

        user_id = request.user.id

        try:

            category = CategoryService.get_category(
                category_id=pk, user_id=user_id)

            if category.user is None and category.is_default:
                user_category, created = Category.objects.get_or_create(
                    user_id=user_id,
                    name=category.name,
                    defaults={
                        'budget': category.budget,
                        'is_default': False,
                        'hidden': False,
                    }
                )

                serializer = CategoryInputSerializer(
                    user_category, data=request.data, partial=True)

            else:
                serializer = CategoryInputSerializer(
                    category, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save(
                    user_id=user_id)

                return response.ok(
                    response_data=serializer.data
                )

            return response.not_found(
                error_details=serializer.errors
            )

        except Category.DoesNotExist:
            return response.not_found(
                error_details=f"No existing category with the id: {pk}"
            )

        except Exception as e:
            return response.internal_error(request, e)

    def destroy(self, request: Request, pk: int) -> Response:
        """
        Handles DELETE requests to soft delete an specific category_id per user

        Args:
            request(Request): The HTTP request object.
            category_id(int): The id of the category that needs to be soft deleted.

        Response: The HTTP Response with no content
        """

        user_id = request.user.id

        try:
            category = CategoryService.get_category(
                category_id=pk, user_id=user_id)

            if category.user is None and category.is_default:
                user_category, created = Category.objects.get_or_create(
                    user_id=user_id,
                    name=category.name,
                    defaults={
                        'budget': category.budget,
                        'is_default': False,
                        'hidden': True,
                    }
                )

                if not created:
                    user_category.hidden = True
                    user_category.save()

            else:
                category.hidden = True
                category.save()

            return response.no_content()

        except Category.DoesNotExist:
            return response.not_found(
                error_details=f"No existing category with the id: {pk}"
            )
        except Exception as e:
            return response.internal_error(request, e)
