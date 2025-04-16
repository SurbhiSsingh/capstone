from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student
from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import Profile
from .forms import StudentRegistrationForm
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
# from .forms import RegistrationForm
import random
import string



# ✅ User registration view
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # ✅ Create profile for new user
            auth_login(request, user)  # ✅ Log in the user immediately
            return redirect("profile")  # ✅ Redirect to profile page
    else:
        form = CustomUserCreationForm()
    
    return render(request, "register/register.html", {"form": form})
# ✅ Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # ✅ Log in the user
            return redirect("profile")  # ✅ Redirect to profile page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "register/login.html")  # ✅ Render login template

# ✅ Profile view
@login_required
def profile(request):
    user_profile, _ = Profile.objects.get_or_create(user=request.user)  # ✅ Ensure Profile exists
    return render(request, "register/profile.html", {"profile": user_profile})

# ✅ Edit profile view
@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)  # ✅ Ensure Profile exists

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("profile")  # ✅ Redirect after successful update
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, "register/edit_profile.html", {"form": form})




############################################################################################
# Generate OTP
def generate_otp():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Send OTP email to the user
def send_otp_email(user_email, otp):
    send_mail(
        "Your OTP Code",
        f"Your OTP code is {otp}",
        "no-reply@iiitd.ac.in",
        [user_email],
    )

# Send registration confirmation to the user
def send_registration_confirmation(user_email):
    send_mail(
        "Registration Successful",
        "You have successfully registered with us!",
        "no-reply@iiitd.ac.in",
        [user_email],
    )

# Send registration notification to the HOD
def send_to_hod_registration(user_email):
    send_mail(
        "New Registration",
        f"A new student has registered: {user_email}",
        "no-reply@iiitd.ac.in",
        [settings.HOD_EMAIL],
    )

# View to handle the registration form submission
def student_registration(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email_domain = form.cleaned_data['email_domain']
            otp = generate_otp()
            email = f"{username}@{email_domain}"
            
            # Send OTP email
            send_otp_email(email, otp)

            # Simulate OTP verification and proceed with registration
            # (In practice, you'll need to handle OTP input and validation)
            send_registration_confirmation(email)
            send_to_hod_registration(email)

            return HttpResponse("Registration Successful. A confirmation email has been sent.")
    else:
        form = StudentRegistrationForm()

    return render(request, "registration.html", {"form": form})



######################################################################################
# def generate_otp(length=6):
#     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# def register(request):
#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             domain = form.cleaned_data['domain']
#             email = f"{username}@{domain}"
#             otp = generate_otp()

#             student, created = Student.objects.update_or_create(
#                 username=username,
#                 defaults={'email': email, 'otp': otp, 'is_verified': False}
#             )

#             # Send OTP email
#             send_mail(
#                 subject="Your OTP for IIITD Registration",
#                 message=f"Your OTP is: {otp}",
#                 from_email="tempemail@yourdomain.com",
#                 recipient_list=[email],
#             )

#             request.session['username'] = username
#             return redirect('verify_otp')
#     else:
#         form = StudentRegistrationForm()
#     return render(request, 'register.html', {'form': form})



#########################################################################################
# def verify_otp(request):
#     username = request.session.get('username')
#     if not username:
#         return redirect('register')

#     student = Student.objects.get(username=username)

#     if request.method == 'POST':
#         input_otp = request.POST.get('otp')
#         if student.otp == input_otp:
#             student.is_verified = True
#             student.save()

#             # Send confirmation emails
#             send_mail(
#                 subject="Registration Confirmed",
#                 message="Welcome! Your registration is complete.",
#                 from_email="tempemail@yourdomain.com",
#                 recipient_list=[student.email],
#             )

#             send_mail(
#                 subject="New Student Registered",
#                 message=f"{student.username} has registered successfully.",
#                 from_email="tempemail@yourdomain.com",
#                 recipient_list=["anuj@iiitd.ac.in"],
#             )

#             messages.success(request, "OTP verified. Registration complete.")
#             return redirect('home')
#         else:
#             messages.error(request, "Invalid OTP. Please try again.")

#     return render(request, 'register\verify_otp.html')  # use full path to template