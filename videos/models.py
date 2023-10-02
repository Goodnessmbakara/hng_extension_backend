from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings



class Video(models.Model):
    """
    Model representing a video. allowing multiple videos.
    """

    screen_recording = models.FileField(upload_to='videos/screen_records')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    transcript = models.TextField(null=True, blank=True)

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom User model where email is the unique identifier and has an is_admin field to allow access to admin.
    """
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)
    profile = models.OneToOneField('Profile', on_delete=models.CASCADE, null=True, blank=True)
    google_id = models.CharField(max_length=255, null=True, blank=True)
    facebook_id = models.CharField(max_length=255, null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ()


class Profile(models.Model):
    """
    Model representing a user's profile. Linked to User via OneToOneField.
    """
    user_profile = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)


class Video(models.Model):
    """
    Model representing a video. Linked to User via ForeignKey, allowing each user to have multiple videos.
    """

    screen_recording = models.FileField(upload_to='videos/screen_records')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    transcript = models.TextField(null=True, blank=True)
