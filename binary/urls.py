from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "binary"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('binary/', views.Prediction.as_view(), name="binary")
]