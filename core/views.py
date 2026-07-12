from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

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