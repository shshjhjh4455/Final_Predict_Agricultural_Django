from django.urls import path
from . import views

app_name = "recommend"

urlpatterns = [
    path("predict/", views.predict, name="predict"),
]