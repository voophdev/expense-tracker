from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Permission, Group

class Users(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    mobile_number = models.CharField(
    max_length=13,
    blank=True,
    null=True,
    validators=[RegexValidator(
            regex=r'^\+?1?\d{9,13}$',
            message="Mobile number must be entered in the format: '+999999999'. Up to 11 digits allowed."
            ),
        ]
    )
    groups = models.ManyToManyField(
        Group, verbose_name='Groups', blank=True, related_name='sigmaly_auth_users', related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission, verbose_name='User Permissions', blank=True, related_name='sigmaly_auth_users', related_query_name='user',
    )

    USERNAME_FIELD = 'email'  # Use email instead of username
    REQUIRED_FIELDS = ['username']  # This is needed for Django's createsuperuser to work

    def __str__(self):
        return self.email