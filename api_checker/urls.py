from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "api_checker"

urlpatterns = [
    path("index", views.index, name="index"),
    path('detail', views.detail, name='detail'),
    path('chart', views.chart, name='chart'),
]
