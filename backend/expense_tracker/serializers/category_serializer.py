from rest_framework import serializers
from expense_tracker.models import Category


class CategoryOutputSerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = ["name", "budget"]


class CategoryInputSerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = ["user", "name", "budget"]
