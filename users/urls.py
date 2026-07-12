from django.urls import path
from .views import UserRegistrationView, UserProfileView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Custom user login
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
    path('profile/', UserProfileView.as_view(), name='user_profile'),  # Get user profile
]
