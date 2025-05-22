from django.db.models import QuerySet
from expense_tracker.models import Category


class CategoryService:
    """
    Business logic related to category model
    """

    @staticmethod
    def list_categories(user_id: int) -> Category[QuerySet]:
        """ Fetch all categories for a specific user """
        return Category.objects.filter(user_id=user_id)

    @staticmethod
    def get_category(category_id: int, user_id: int) -> Category:
        """ Fetch a specific category based on category_id provided"""
        return Category.objects.get(id=category_id, user_id=user_id)
