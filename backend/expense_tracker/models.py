from django.db import models
from authentication.models import Users


class Category(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    is_default = models.BooleanField(default=False)
    hidden = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'name'], name='unique_user_category')
        ]

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, blank=False, null=True)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField()
    note = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
