from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import UserProfile


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()
