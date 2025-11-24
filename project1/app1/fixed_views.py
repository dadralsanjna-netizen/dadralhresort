# # def test_email(request):
# #     try:
# #         # Test settings configuration
# #         if not django_settings.EMAIL_HOST_USER:
# #             return HttpResponse("Error: EMAIL_HOST_USER is not set in settings.py")
# #         if not django_settings.EMAIL_HOST_PASSWORD:
# #             return HttpResponse("Error: EMAIL_HOST_PASSWORD is not set in settings.py")
        
# #         # Try to send test email
# #         subject = 'Test Email from Raj Vilas Palace'
# #         message = 'This is a test email from your Django application.'
# #         from_email = django_settings.DEFAULT_FROM_EMAIL
# #         recipient_list = [django_settings.EMAIL_HOST_USER]
        
# #         send_mail(
# #             subject,
# #             message,
# #             from_email,
# #             recipient_list,
# #             fail_silently=False,
# #         )
        
# #         return HttpResponse(
# #             f"Test email attempt completed:<br>"
# #             f"From: {from_email}<br>"
# #             f"To: {recipient_list[0]}<br>"
# #             f"Subject: {subject}<br>"
# #             f"Using backend: {django_settings.EMAIL_BACKEND}"
# #         )
# #     except Exception as e:
# #         import traceback
# #         trace = traceback.format_exc()
# #         return HttpResponse(
# #             f"Email error:<br>"
# #             f"Error type: {type(e).__name__}<br>"
# #             f"Error message: {str(e)}<br>"
# #             f"Traceback:<br><pre>{trace}</pre>"
# #         )

# # def forgot(request):
# #     message = None
# #     message_type = None
    
# #     if request.method == 'POST':
# #         email = request.POST['email']
# #         user = User.objects.filter(email=email).first()
        
# #         if user:
# #             try:
# #                 subject = 'Password Reset Request - Raj Vilas Palace'
# #                 # Generate proper URL using the request host
# #                 reset_link = request.build_absolute_uri(f'/password_reset/{user.id}/')
                
# #                 # Plain text version
# #                 text_message = f'''
# # Hello {user.username},

# # You requested a password reset for your account at Dadralh Resort.

# # Click the following link to reset your password:
# # {reset_link}

# # If you did not request this password reset, please ignore this email.

# # Best regards,
# # Dadralh Resort Team
# #                 '''
                
# #                 # HTML version with clickable link
# #                 html_message = f'''
# #                 <html>
# #                     <body style="font-family: Arial, sans-serif; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; margin: 0;">
# #                         <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
# #                             <div style="text-align: center; margin-bottom: 30px;">
# #                                 <h1 style="color: #667eea; margin: 0; font-size: 28px; font-weight: bold;">🌴 Dadralh Resort</h1>
# #                             </div>
# #                             <h2 style="color: #2c3e50; margin-bottom: 20px; border-bottom: 3px solid #667eea; padding-bottom: 10px;">Password Reset Request</h2>
# #                             <p style="color: #333; line-height: 1.8; margin-bottom: 15px; font-size: 16px;">Hello <strong style="color: #667eea;">{user.username}</strong>,</p>
# #                             <p style="color: #555; line-height: 1.8; margin-bottom: 25px; font-size: 15px;">
# #                                 You requested a password reset for your account at <strong style="color: #667eea;">Dadralh Resort</strong>.
# #                             </p>
# #                             <div style="text-align: center; margin: 35px 0;">
# #                                 <a href="{reset_link}" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 16px 40px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; font-size: 16px; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); transition: transform 0.3s;">
# #                                     🔐 Reset My Password
# #                                 </a>
# #                             </div>
# #                             <p style="color: #777; font-size: 13px; margin-top: 30px; border-top: 2px solid #f0f0f0; padding-top: 20px; line-height: 1.6;">
# #                                 If the button doesn't work, copy and paste this link into your browser:<br>
# #                                 <a href="{reset_link}" style="color: #667eea; word-break: break-all; text-decoration: none;">{reset_link}</a>
# #                             </p>
# #                             <p style="color: #999; font-size: 13px; margin-top: 20px; font-style: italic;">
# #                                 If you did not request this password reset, please ignore this email.
# #                             </p>
# #                             <p style="color: #777; font-size: 13px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
# #                                 Best regards,<br>
# #                                 <strong style="color: #667eea; font-size: 14px;">Dadralh Resort Team 🌴</strong>
# #                             </p>
# #                         </div>
# #                     </body>
# #                 </html>
# #                 '''
                
# #                 # Send HTML email with clickable link
# #                 msg = EmailMultiAlternatives(
# #                     subject,
# #                     text_message,
# #                     django_settings.DEFAULT_FROM_EMAIL,
# #                     [email]
# #                 )
# #                 msg.attach_alternative(html_message, "text/html")
# #                 msg.send()
                
# #                 message = "Password reset link has been sent to your email address!"
# #                 message_type = "success"
# #                 print(f"\n{'='*60}")
# #                 print("EMAIL SENT SUCCESSFULLY!")
# #                 print(f"To: {email}")
# #                 print(f"Subject: {subject}")
# #                 print(f"Reset Link: {reset_link}")
# #                 print(f"{'='*60}\n")
# #             except Exception as e:
# #                 # Log the error for debugging
# #                 print(f"\n{'='*60}")
# #                 print("EMAIL SENDING FAILED!")
# #                 print(f"Error: {str(e)}")
# #                 print(f"Error Type: {type(e).__name__}")
# #                 print(f"{'='*60}\n")
# #                 message = f"Failed to send email. Error: {str(e)}"
# #                 message_type = "error"
# #         else:
# #             message = "Email address not found in our system. Please check your email and try again."
# #             message_type = "error"
    
# #     context = {
# #         'message': message,
# #         'message_type': message_type
# #     }
# #     return render(request, 'forgot_password.html', context)


# from django.http import HttpResponse
# from django.conf import settings  # Correct import
# from django.core.mail import send_mail, EmailMultiAlternatives
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User

# def test_email(request):
#     try:
#         # Test settings configuration - FIXED: use settings instead of django_settings
#         if not settings.EMAIL_HOST_USER:
#             return HttpResponse("Error: EMAIL_HOST_USER is not set in settings.py")
#         if not settings.EMAIL_HOST_PASSWORD:
#             return HttpResponse("Error: EMAIL_HOST_PASSWORD is not set in settings.py")
        
#         # Try to send test email
#         subject = 'Test Email from Raj Vilas Palace'
#         message = 'This is a test email from your Django application.'
#         from_email = settings.DEFAULT_FROM_EMAIL
#         recipient_list = [settings.EMAIL_HOST_USER]
        
#         send_mail(
#             subject,
#             message,
#             from_email,
#             recipient_list,
#             fail_silently=False,
#         )
        
#         return HttpResponse(
#             f"Test email attempt completed:<br>"
#             f"From: {from_email}<br>"
#             f"To: {recipient_list[0]}<br>"
#             f"Subject: {subject}<br>"
#             f"Using backend: {settings.EMAIL_BACKEND}"
#         )
#     except Exception as e:
#         import traceback
#         trace = traceback.format_exc()
#         return HttpResponse(
#             f"Email error:<br>"
#             f"Error type: {type(e).__name__}<br>"
#             f"Error message: {str(e)}<br>"
#             f"Traceback:<br><pre>{trace}</pre>"
#         )

# def forgot(request):
#     message = None
#     message_type = None
    
#     if request.method == 'POST':
#         email = request.POST['email']
#         user = User.objects.filter(email=email).first()
        
#         if user:
#             try:
#                 subject = 'Password Reset Request - Raj Vilas Palace'
#                 # Generate proper URL using the request host
#                 reset_link = request.build_absolute_uri(f'/password_reset/{user.id}/')
                
#                 # Plain text version
#                 text_message = f'''
# Hello {user.username},

# You requested a password reset for your account at Dadralh Resort.

# Click the following link to reset your password:
# {reset_link}

# If you did not request this password reset, please ignore this email.

# Best regards,
# Dadralh Resort Team
#                 '''
                
#                 # HTML version with clickable link
#                 html_message = f'''
#                 <html>
#                     <body style="font-family: Arial, sans-serif; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; margin: 0;">
#                         <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
#                             <div style="text-align: center; margin-bottom: 30px;">
#                                 <h1 style="color: #667eea; margin: 0; font-size: 28px; font-weight: bold;">🌴 Dadralh Resort</h1>
#                             </div>
#                             <h2 style="color: #2c3e50; margin-bottom: 20px; border-bottom: 3px solid #667eea; padding-bottom: 10px;">Password Reset Request</h2>
#                             <p style="color: #333; line-height: 1.8; margin-bottom: 15px; font-size: 16px;">Hello <strong style="color: #667eea;">{user.username}</strong>,</p>
#                             <p style="color: #555; line-height: 1.8; margin-bottom: 25px; font-size: 15px;">
#                                 You requested a password reset for your account at <strong style="color: #667eea;">Dadralh Resort</strong>.
#                             </p>
#                             <div style="text-align: center; margin: 35px 0;">
#                                 <a href="{reset_link}" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 16px 40px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; font-size: 16px; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); transition: transform 0.3s;">
#                                     🔐 Reset My Password
#                                 </a>
#                             </div>
#                             <p style="color: #777; font-size: 13px; margin-top: 30px; border-top: 2px solid #f0f0f0; padding-top: 20px; line-height: 1.6;">
#                                 If the button doesn't work, copy and paste this link into your browser:<br>
#                                 <a href="{reset_link}" style="color: #667eea; word-break: break-all; text-decoration: none;">{reset_link}</a>
#                             </p>
#                             <p style="color: #999; font-size: 13px; margin-top: 20px; font-style: italic;">
#                                 If you did not request this password reset, please ignore this email.
#                             </p>
#                             <p style="color: #777; font-size: 13px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
#                                 Best regards,<br>
#                                 <strong style="color: #667eea; font-size: 14px;">Dadralh Resort Team 🌴</strong>
#                             </p>
#                         </div>
#                     </body>
#                 </html>
#                 '''
                
#                 # Send HTML email with clickable link - FIXED: use settings instead of django_settings
#                 msg = EmailMultiAlternatives(
#                     subject,
#                     text_message,
#                     settings.DEFAULT_FROM_EMAIL,  # FIXED
#                     [email]
#                 )
#                 msg.attach_alternative(html_message, "text/html")
#                 msg.send()
                
#                 message = "Password reset link has been sent to your email address!"
#                 message_type = "success"
#                 print(f"\n{'='*60}")
#                 print("EMAIL SENT SUCCESSFULLY!")
#                 print(f"To: {email}")
#                 print(f"Subject: {subject}")
#                 print(f"Reset Link: {reset_link}")
#                 print(f"{'='*60}\n")
#             except Exception as e:
#                 # Log the error for debugging
#                 print(f"\n{'='*60}")
#                 print("EMAIL SENDING FAILED!")
#                 print(f"Error: {str(e)}")
#                 print(f"Error Type: {type(e).__name__}")
#                 print(f"{'='*60}\n")
#                 message = f"Failed to send email. Error: {str(e)}"
#                 message_type = "error"
#         else:
#             message = "Email address not found in our system. Please check your email and try again."
#             message_type = "error"
    
#     context = {
#         'message': message,
#         'message_type': message_type
#     }
#     return render(request, 'forgot_password.html', context)

from django.http import HttpResponse
from django.conf import settings as django_settings  # Rename to avoid conflict
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import smtplib

def test_email(request):
    try:
        # Use django_settings instead of settings
        print(f"Testing email configuration:")
        print(f"EMAIL_HOST: {django_settings.EMAIL_HOST}")
        print(f"EMAIL_HOST_USER: {django_settings.EMAIL_HOST_USER}")
        
        # Test SMTP connection
        try:
            server = smtplib.SMTP(django_settings.EMAIL_HOST, django_settings.EMAIL_PORT)
            server.starttls()
            server.login(django_settings.EMAIL_HOST_USER, django_settings.EMAIL_HOST_PASSWORD)
            server.quit()
            print("SMTP connection test: SUCCESS")
        except Exception as smtp_error:
            return HttpResponse(f"SMTP Connection Failed: {smtp_error}")
        
        # Send test email
        subject = 'Test Email from Raj Vilas Palace'
        message = 'This is a test email from your Django application.'
        from_email = django_settings.DEFAULT_FROM_EMAIL
        recipient_list = [django_settings.EMAIL_HOST_USER]
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        
        return HttpResponse("✅ Test email sent successfully!")
        
    except Exception as e:
        return HttpResponse(f"❌ Email sending failed: {e}")

def forgot(request):
    message = None
    message_type = None
    
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            message = "Please enter an email address."
            message_type = "error"
        else:
            user = User.objects.filter(email=email).first()
            
            if user:
                try:
                    subject = 'Password Reset Request - Raj Vilas Palace'
                    reset_link = request.build_absolute_uri(f'/password_reset/{user.id}/')
                    
                    # Plain text version
                    text_message = f'''
Hello {user.username},

You requested a password reset for your account at Dadralh Resort.

Click the following link to reset your password:
{reset_link}

If you did not request this password reset, please ignore this email.

Best regards,
Dadralh Resort Team
                    '''
                    
                    # HTML version
                    html_message = f'''
                    <html>
                        <body style="font-family: Arial, sans-serif; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; margin: 0;">
                            <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                                <div style="text-align: center; margin-bottom: 30px;">
                                    <h1 style="color: #667eea; margin: 0; font-size: 28px; font-weight: bold;">🌴 Dadralh Resort</h1>
                                </div>
                                <h2 style="color: #2c3e50; margin-bottom: 20px; border-bottom: 3px solid #667eea; padding-bottom: 10px;">Password Reset Request</h2>
                                <p style="color: #333; line-height: 1.8; margin-bottom: 15px; font-size: 16px;">Hello <strong style="color: #667eea;">{user.username}</strong>,</p>
                                <p style="color: #555; line-height: 1.8; margin-bottom: 25px; font-size: 15px;">
                                    You requested a password reset for your account at <strong style="color: #667eea;">Dadralh Resort</strong>.
                                </p>
                                <div style="text-align: center; margin: 35px 0;">
                                    <a href="{reset_link}" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 16px 40px; text-decoration: none; border-radius: 8px; display: inline-block; font-weight: bold; font-size: 16px; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">
                                        🔐 Reset My Password
                                    </a>
                                </div>
                                <p style="color: #777; font-size: 13px; margin-top: 30px; border-top: 2px solid #f0f0f0; padding-top: 20px; line-height: 1.6;">
                                    If the button doesn't work, copy and paste this link into your browser:<br>
                                    <a href="{reset_link}" style="color: #667eea; word-break: break-all; text-decoration: none;">{reset_link}</a>
                                </p>
                                <p style="color: #999; font-size: 13px; margin-top: 20px; font-style: italic;">
                                    If you did not request this password reset, please ignore this email.
                                </p>
                                <p style="color: #777; font-size: 13px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee;">
                                    Best regards,<br>
                                    <strong style="color: #667eea; font-size: 14px;">Dadralh Resort Team 🌴</strong>
                                </p>
                            </div>
                        </body>
                    </html>
                    '''
                    
                    # Use django_settings instead of settings
                    msg = EmailMultiAlternatives(
                        subject,
                        text_message,
                        django_settings.DEFAULT_FROM_EMAIL,  # FIXED
                        [email]
                    )
                    msg.attach_alternative(html_message, "text/html")
                    msg.send()
                    
                    message = "✅ Password reset link has been sent to your email address!"
                    message_type = "success"
                    print(f"EMAIL SENT SUCCESSFULLY to {email}")
                    
                except Exception as e:
                    print(f"EMAIL SENDING FAILED: {e}")
                    message = f"❌ Failed to send email. Error: {str(e)}"
                    message_type = "error"
            else:
                message = "❌ Email address not found in our system."
                message_type = "error"
    
    return render(request, 'forgot_password.html', {'message': message, 'message_type': message_type})