from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegistrationAPIView  # <--- new line
from . import views     # <--- new line
from django.urls import path

urlpatterns = [
    path('users/register', RegistrationAPIView.as_view()),  # <--- new

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
