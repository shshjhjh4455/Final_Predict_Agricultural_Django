from django.urls import path, include
from . import views
from rest_framework import urls

# from django.urls import include, path

urlpatterns = [
    path("signup/", views.UserCreate.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("login/<int:pk>/", views.Detailaccounts.as_view()),
    # rest_auth.registration.urls 에서 제공하는 url을 사용하기 위해 include
    # path("login/", include("rest_auth.registration.urls")),
]
