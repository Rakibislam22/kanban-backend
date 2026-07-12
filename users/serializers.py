from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles validation for user fields and password confirmation.
    """
    # Add a write-only password confirmation field.
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm Password")

    class Meta:
        model = User
        # Define fields to be used for registration.
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            # Ensure password is write-only and has password validators.
            'password': {'write_only': True, 'validators': [validate_password]},
            # Mark other fields as required.
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        """
        Custom validation to check if passwords match.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        """
        Create and return a new user with a hashed password.
        """
        # The create_user manager method handles password hashing automatically.
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the user profile details.
    Provides read-only access to essential user information.
    """
    class Meta:
        model = User
        # Define the fields to be exposed in the user profile endpoint.
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        # Ensure these fields are read-only.
        read_only_fields = fields

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customizes the token response to include user's details.
    """
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super().validate(attrs)

        # Add user details to the response
        serializer = UserProfileSerializer(self.user)
        data['user'] = serializer.data

        return data
