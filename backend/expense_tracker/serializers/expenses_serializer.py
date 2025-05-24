from datetime import datetime, date
from rest_framework import serializers
from expense_tracker.models import Expense


class ExpenseOutputSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    purchased_at = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields = ["id", "name", "amount", "purchased_at",
                  "note", "category"]

    def get_category(self, obj):
        return obj.category.name if obj.category else None

    def get_purchased_at(self, obj):
        return obj.purchased_at.strftime("%B,  %d, %Y") if obj.purchased_at else None


class ExpenseInputSerializer(serializers.ModelSerializer):

    purchased_at = serializers.CharField()

    class Meta:
        model = Expense
        fields = ["id", "user", "name", "amount",
                  "purchased_at", "note", "category"]

    def validate_purchased_at(self, value):
        try:
            parsed_date = datetime.strptime(value, "%B %d, %Y").date()
        except ValueError:
            raise serializers.ValidationError(
                "Date must be in 'Month dd, yyyy' format (e.g., December 25, 2024).")
        return parsed_date
