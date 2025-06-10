from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import RegisterForm, LoginForm, ProfileUpdateForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = Profile.objects.get(username=username)
                if check_password(password, user.password):
                    request.session["profile_id"] = user.id
                    return redirect("profile_view")
                else:
                    messages.error(request, "Invalid password.")
            except Profile.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    return render(request, "register/login.html", {"form": form})


def logout_view(request):
    request.session.flush()
    return redirect("login")


def get_logged_in_profile(request):
    profile_id = request.session.get("profile_id")
    if profile_id:
        try:
            return Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return None
    return None


def profile_view(request):
    profile = get_logged_in_profile(request)
    if not profile:
        return redirect("login")
    return render(request, "register/profile.html", {"profile": profile})


def edit_profile(request):
    profile = get_logged_in_profile(request)
    if not profile:
        return redirect("login")

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile_view")
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, "register/edit_profile.html", {"form": form})


def change_password(request):
    profile = get_logged_in_profile(request)
    if not profile:
        return redirect("login")

    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not check_password(old_password, profile.password):
            messages.error(request, "Old password is incorrect.")
        elif new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
        elif len(new_password) < 6:
            messages.error(request, "New password must be at least 6 characters.")
        else:
            profile.password = make_password(new_password)
            profile.save()
            messages.success(request, "Password changed successfully!")
            return redirect("profile_view")
    return render(request, "register/change_password.html")
