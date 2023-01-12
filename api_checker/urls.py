from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "api_checker"

urlpatterns = [
    path("index", views.index, name="index"),
    path('detail', views.detail, name='detail'),
    path('chart_index', views.chart_index, name="chart_index"),
    path('chart_5', views.chart_5days, name='chart_5'),
    path('chart_20', views.chart_20days, name='chart_20'),
    path('chart_365', views.chart_365days, name='chart_365'),
]
