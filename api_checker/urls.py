from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "api_checker"

urlpatterns = [
    path("detail", views.detail, name="detail"),
]
