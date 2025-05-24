from authentication.models import Users
from typing import List, Optional


class UsersService:

    @staticmethod
    def get_user(email: str, values: Optional[List[str]] = None) -> Users:
        user = Users.objects.filter(email=email)
        if values:
            return user.values(*values)
        return user
