from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings 
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.apps import apps

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  # ✅ Add this line

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
    # ✅ Fix reverse accessor clash
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)



# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=10, unique=True)

#     groups = models.ManyToManyField(
#         "auth.Group",
#         related_name="customuser_set",  # Avoids clash with built-in User model
#         blank=True,
#     )
#     user_permissions = models.ManyToManyField(
#         "auth.Permission",
#         related_name="customuser_permissions_set",  # Avoids clash
#         blank=True,
#     )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # ✅ Fixed
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@login_required
def edit_profile(request):
    user = request.user  # Ensure using correct user instance

    # Fetch Profile or create if not exists
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        profile.email = request.POST.get("email")
        profile.phone = request.POST.get("phone")
        profile.save()
        return redirect('profile')  # Redirect to profile page

    return render(request, 'register/edit_profile.html', {'profile': profile})


######################################################################################################################
class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
