from django.urls import path, include
from . import views
from rest_framework import urls

# urlpatterns = [
#     path('', include('dj_rest_auth.urls')), # 해당 라인 추가
#     path('registration/', include('dj_rest_auth.registration.urls')),
# ]


urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
 ]