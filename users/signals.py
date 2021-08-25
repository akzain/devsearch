from users.views import profiles
from django.db.models.signals import post_save, post_delete

from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import message, send_mail
from django.conf import settings


def createProfile(sender, instance, created, **kwargs):
    print("Profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user, username=user.username, email=user.email, name=user.first_name,
        )
        subject = 'Welcome to devsearch'
        message = 'We\'re glad you are here. We advise you to check the about and the rules sections first before getting active on the devsearch platform. We hope you get some profit from devsearc!!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)

