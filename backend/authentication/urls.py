from django.urls import path
from authentication.api import auth

urlpatterns = [
    path('login/', auth.Login.as_view(), name="login"),
]
