import random
import string
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_otp_email(to_email, otp):
    send_mail(
        subject='Your OTP Code',
        message=f'Your OTP is: {otp}',
        from_email='temp@example.com',  # Use temp email here
        recipient_list=[to_email]
    )
