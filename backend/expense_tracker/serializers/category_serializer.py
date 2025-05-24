from rest_framework import serializers
from expense_tracker.models import Category


class CategoryOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "budget"]


class CategoryInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "user", "name", "budget"]
