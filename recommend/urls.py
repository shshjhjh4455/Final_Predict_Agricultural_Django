from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "recommend"

urlpatterns = [
    path("predict/", views.predict, name="predict"),
]
