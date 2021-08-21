from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


from django.core.exceptions import ValidationError

from urllib.parse import urlparse


def validate_url_github(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ("github.com", "www.github.com"):
        raise ValidationError("Only urls from Github are allowed")


def validate_url_twitter(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ("twitter.com", "www.twitter.com"):
        raise ValidationError("Only urls from twitter are allowed")


def validate_url_linkedin(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ("linkedin.com", "www.linkedin.com"):
        raise ValidationError("Only urls from linkedin are allowed")


def validate_url_yt(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ("youtube.com", "www.youtube.com"):
        raise ValidationError("Only urls from youtube are allowed")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profiles/",
        default="profiles/user-default.png",
    )
    social_github = models.URLField(
        max_length=200, blank=True, null=True, validators=[validate_url_github]
    )
    social_twitter = models.URLField(
        max_length=200, blank=True, null=True, validators=[validate_url_twitter]
    )
    social_linkedin = models.URLField(
        max_length=200, blank=True, null=True, validators=[validate_url_linkedin]
    )
    social_youtube = models.URLField(
        max_length=200, blank=True, null=True, validators=[validate_url_yt]
    )
    social_website = models.URLField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True
    )
    recipient = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["is_read", "-created"]
