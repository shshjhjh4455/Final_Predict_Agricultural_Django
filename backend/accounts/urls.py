from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path("signup/", views.UserCreate.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    # login 버튼 누른 후 url로 이동
    path("login/", views.LoginView.as_view()),
]
