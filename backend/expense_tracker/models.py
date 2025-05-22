from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)


class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField()
    note = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
