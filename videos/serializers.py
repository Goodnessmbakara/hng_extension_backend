from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile,Video

from django.contrib.auth import get_user_model

User = get_user_model()



class VideoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Video model.

    Fields:
        user: The user who uploaded the video.
        screen_recording: The video file (screen recording).
        uploaded_at: The timestamp when the video was uploaded.
    """
    screen_recording = serializers.FileField()
    uploaded_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Video
        fields = ('id','screen_recording', 'uploaded_at')

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model with additional user-related fields.

    Fields:
        bio: The user's biography.
        profile_picture: The user's profile picture.
        username: The username of the associated user.
        email: The email address of the associated user.
    """
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture', 'username', 'email')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Fields:
        email: The email address of the user.
        password: The user's password (write-only field).
        username: The username of the user.
    """
    class Meta:
        model = User
        fields = ['email', 'password', 'username']
        extra_kwargs = {'password': {'write_only': True}}

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    Fields:
        username: The desired username for the new user.
        email: The email address of the new user.
        password: The password for the new user (write-only field).
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create and return a new user instance upon successful registration.

        Args:
            validated_data: The validated data containing user registration details.

        Returns:
            User: The newly created user instance.
        """
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user