# # from django.db.models.signals import post_save
# # from django.dispatch import receiver
# # from django.contrib.auth.models import User
# # from django.contrib.auth import get_user_model
# # from .models import Profile
# # User = get_user_model()


# # @receiver(post_save, sender=User)
# # def create_user_profile(sender, instance, created, **kwargs):
# #     if created:
# #         Profile.objects.create(user=instance)

# # @receiver(post_save, sender=User)
# # def save_user_profile(sender, instance, **kwargs):
# #     instance.profile.save()
# # register/signals.py

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created and not instance.is_superuser:  # <-- this check added
#         Profile.objects.create(user=instance, phone="", address="")

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Profile, CustomUser


@receiver(post_save, sender=CustomUser)   # Important: CustomUser not User
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)   # Optional: Auto save profile on user save
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
