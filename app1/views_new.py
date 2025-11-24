from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Booking, Room, Gallery, ContactMessage, rooms, billing
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.utils import timezone

# ... (keep all the existing imports and functions up to the forgot function)

def test_email(request):
    """Test email configuration and sending."""
    try:
        # Test settings configuration
        if not settings.EMAIL_HOST_USER:
            return HttpResponse("Error: EMAIL_HOST_USER is not set in settings.py")
        if not settings.EMAIL_HOST_PASSWORD:
            return HttpResponse("Error: EMAIL_HOST_PASSWORD is not set in settings.py")
        
        # Try to send test email
        subject = 'Test Email from Raj Vilas Palace'
        message = 'This is a test email from your Django application.'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.EMAIL_HOST_USER]
        
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        
        return HttpResponse(
            f"Test email attempt completed:<br>"
            f"From: {from_email}<br>"
            f"To: {recipient_list[0]}<br>"
            f"Subject: {subject}<br>"
            f"Using backend: {settings.EMAIL_BACKEND}"
        )
    except Exception as e:
        import traceback
        trace = traceback.format_exc()
        return HttpResponse(
            f"Email error:<br>"
            f"Error type: {type(e).__name__}<br>"
            f"Error message: {str(e)}<br>"
            f"Traceback:<br><pre>{trace}</pre>"
        )

def forgot(request):
    """Handle forgot password functionality."""
    message = None
    message_type = None
    
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        
        if user:
            try:
                subject = 'Password Reset Request - Dadralh Resort'
                reset_link = request.build_absolute_uri(f'/password_reset/{user.id}/')
                
                # Plain text version
                text_content = f'''
Hello {user.username},

You requested a password reset for your account at Dadralh Resort.
Click the link below to reset your password:

{reset_link}

If you did not request this reset, please ignore this email.

Best regards,
Dadralh Resort Team
                '''
                
                # Create email message
                msg = EmailMultiAlternatives(
                    subject,
                    text_content,
                    settings.DEFAULT_FROM_EMAIL,
                    [email]
                )
                
                # HTML version
                html_content = f'''
                <html>
                    <body style="font-family: Arial, sans-serif; padding: 20px;">
                        <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
                            <h1 style="color: #0066cc; margin-bottom: 20px;">Password Reset Request</h1>
                            <p>Hello {user.username},</p>
                            <p>You requested a password reset for your Dadralh Resort account.</p>
                            <div style="text-align: center; margin: 30px 0;">
                                <a href="{reset_link}" style="background: #0066cc; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px;">Reset Password</a>
                            </div>
                            <p style="color: #666; font-size: 14px;">If the button doesn't work, copy and paste this link:<br>
                            <a href="{reset_link}">{reset_link}</a></p>
                            <p style="color: #999; font-style: italic;">If you did not request this reset, please ignore this email.</p>
                        </div>
                    </body>
                </html>
                '''
                
                # Attach HTML version
                msg.attach_alternative(html_content, "text/html")
                
                # Send email
                msg.send()
                
                message = "Password reset instructions have been sent to your email!"
                message_type = "success"
                print(f"Password reset email sent successfully to {email}")
                
            except Exception as e:
                message = "Failed to send email. Please try again later."
                message_type = "error"
                print(f"Email error: {str(e)}")
        else:
            message = "No account found with this email address."
            message_type = "error"
    
    return render(request, 'forgot_password.html', {
        'message': message,
        'message_type': message_type
    })

def reset(request, id):
    """Handle password reset."""
    user = get_object_or_404(User, id=id)
    error_message = None
    
    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            error_message = "Passwords do not match!"
        elif len(password) < 8:  # Increased minimum length for security
            error_message = "Password must be at least 8 characters long!"
        else:
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successfully! Please login with your new password.')
            return redirect('logins')
    
    return render(request, 'password_reset.html', {
        'user': user,
        'error': error_message
    })

# ... (keep all remaining functions as is)