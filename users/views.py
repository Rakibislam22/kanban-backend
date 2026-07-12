from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer, UserProfileSerializer, CustomTokenObtainPairSerializer

# --- User Registration View (existing code) ---
class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for creating (registering) a new user.
    This endpoint is public and does not require authentication,
    as specified by the AllowAny permission class.
    """
    queryset = User.objects.all()
    # Override the default permission (IsAuthenticated) to allow anyone to register.
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

# --- Custom Login View ---
class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom login view that uses the custom serializer to include user details in the token.
    """
    serializer_class = CustomTokenObtainPairSerializer

# --- New User Profile View ---
class UserProfileView(APIView):
    """
    API endpoint to retrieve the authenticated user's profile details.
    This view is protected and requires a valid JWT token.
    """
    # Ensure only authenticated users can access this endpoint.
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and returns the authenticated user's data.
        """
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
