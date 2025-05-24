from django.db.models import QuerySet
from expense_tracker.models import Category


class CategoryService:
    """
    Business logic related to category model
    """

    @staticmethod
    def list_categories(user_id: int) -> QuerySet:
        """
        Fetch all categories for a specific user, including shared defaults not overridden or hidden by the user.
        """

        user_categories = Category.objects.filter(
            user_id=user_id, hidden=False)

        user_category_names = Category.objects.filter(
            user_id=user_id).values_list('name', flat=True)

        default_categories = Category.objects.filter(
            user=None, is_default=True, hidden=False
        ).exclude(name__in=user_category_names)

        return user_categories | default_categories

    @staticmethod
    def get_category(category_id: int, user_id: int) -> Category:
        """
        Fetch a specific category for a user.
        First, try to get the user's own category.
        If not found, try to get the shared default (if allowed).
        """
        try:
            return Category.objects.get(
                id=category_id, user_id=user_id, hidden=False)

        except Category.DoesNotExist:
            try:
                return Category.objects.get(
                    id=category_id, user=None, is_default=True, hidden=False)
            except Category.DoesNotExist:
                raise Category.DoesNotExist(
                    f"No category found with id={category_id} for user or as default.")
