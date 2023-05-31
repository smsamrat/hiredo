from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client


def send_otp_via_email(email, otp):
    subject = "Password Reset Request"
    message = f"""Dear valued customer,\n\nWe received a request to reset the password for your account. To complete this process, please use the following One-Time Password (OTP):\n\n{otp}\n\nPlease note that this OTP will expire in 1 minutes for security purposes. If you did not request this password reset, please contact our support team immediately.\n\nThank you for trusting us with your account security.\n\nBest regards,\nThe HireDo Team"""
    email_from = settings.DEFAULT_FROM_EMAIL
    try:
        send_mail(subject, message, email_from, [email])
    except Exception as e:
        return str(e)


def send_otp_via_sms(phone_number, otp):
    account_sid = 'ACccf0994b6176348f52352dd2fa2cf87c'
    auth_token = '177f671239ca48c64524294748140a35'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+13657997182',
    body=f"Your OTP: {otp}. Please enter this code to proceed with HireDo verification. Do not share this code with anyone. Thank you.",
    to=phone_number
    )
