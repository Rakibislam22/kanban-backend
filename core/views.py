from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for creating (registering) a new user.
    This endpoint is public and does not require authentication.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Override default permission to allow anyone to register
    serializer_class = UserRegistrationSerializer