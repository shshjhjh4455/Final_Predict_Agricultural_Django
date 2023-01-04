from django.urls import path
from . import views


app_name = "recommend"

urlpatterns = [
<<<<<<< HEAD
]
=======
    path("", views.index, name="index"),
    path("predict/", views.predict, name="predict"),
    path("result/", views.result, name="result"),
]
>>>>>>> parent of e2cfe84e (recommend setting)
