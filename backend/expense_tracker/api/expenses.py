from rest_framework.viewsets import ModelViewSet
from expense_tracker.models import Expense
from expense_tracker.serializers.expenses_serializer import ExpenseInputSerializer, ExpenseOutputSerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ExpenseOutputSerializer
        return ExpenseInputSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Expense.objects.filter(user_id=user_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
