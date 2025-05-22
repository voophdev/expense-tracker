from django.db.models import QuerySet
from expense_tracker.models import Expense


class ExpenseService:
    """ 
    Business logic related to expense model.
    """

    @staticmethod
    def list_expenses(user_id: int) -> QuerySet[Expense]:
        """ Fetch all expenses for a specific user. """
        return Expense.objects.filter(user_id=user_id)

    @staticmethod
    def get_expense(expense_id: int, user_id: int) -> Expense:
        """ Fetch a specific expense for a specific user. """
        return Expense.objects.get(id=expense_id, user_id=user_id)
