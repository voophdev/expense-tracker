from rest_framework import serializers
from expense_tracker.models import Expense


class ExpenseOutputSerializer(serializers.Serializer):

    category = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields = ["name", "amount", "purchased_at",
                  "note", "category"]

    def get_category(self, obj):
        return obj.category.name if obj.category else None


class ExpenseInputSerializer(serializers.Serializer):

    class Meta:
        model = Expense
        fields = ["user", "name", "amount",
                  "purchased_at", "note", "category"]
