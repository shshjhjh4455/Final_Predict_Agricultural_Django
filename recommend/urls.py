from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "recommend"

urlpatterns = [
   path("result/", views.result, name="result"),
]
