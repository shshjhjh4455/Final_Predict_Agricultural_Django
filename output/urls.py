from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "output"

urlpatterns = [
    path("oupredict/", views.oupredict, name="oupredict"),
]
