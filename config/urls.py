from django.contrib import admin
from django.urls import path, include

from furoot.views import base_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("furoot/", include("furoot.urls")),
    path("common/", include("common.urls")),
    path("recommend/", include("recommend.urls")),
    path("output/", include("output.urls")),
    path("predict/", include("predict.urls")),
    path("api_checker/", include("api_checker.urls")),
    path("", base_views.index, name="index"),  # '/' 에 해당되는 path
]
