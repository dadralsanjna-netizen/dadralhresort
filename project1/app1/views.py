from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Booking, A, billing, Room, Gallery, ContactMessage
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.conf import settings as django_settings  # Renamed to avoid conflict



# # Create your views here.
# def index(request):
#     return render(request,'index.html')
# def header(request):
#     return render(request,'header.html')
# def menu(request):
#     return render(request,'menu2.html')
# # def register(request):
# #     if request.method=="POST":
# #         name=request.POST['name']
# #         email=request.POST['email']
# #         phn=request.POST['phn']
# #         password=request.POST['password']
# #         cpassword=request.POST['cpassword']
# #         if password==cpassword:
# #            if  User.objects.filter(username=name).exists():
# #                 return HttpResponse("username already exit.please choose another.")
# #            if  User.objects.filter(email=email).exists():
# #                 return HttpResponse("Email already registered.please use another.")
# #             user.objects.create_user(username=name,email=email,password=password).save()
# #             return redirect(logins)
# #         else:
# #             return HttpResponse("Password should be same")

# #     return render(request,'register.html')
# def register(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         phn = request.POST['phn']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
#         if password == cpassword:
#             if User.objects.filter(username=name).exists():
#                 return HttpResponse("Username already exists. Please choose another.")
#             if User.objects.filter(email=email).exists():
#                 return HttpResponse("Email already registered. Please use another.")
#             User.objects.create_user(username=name, email=email, password=password).save()
#             return redirect(logins)
#         else:
#             return HttpResponse("Password should be same")
#     return render(request, 'register.html')

# def book(request,id):
#     if request.method == 'POST':
#         checkin = request.POST.get('checkin')
#         checkout = request.POST.get('checkout')
#         guest = request.POST.get('guest')
#         nights = request.POST.get('nights')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         requests_text = request.POST.get('requests')

#         # Save booking
#         booking = Booking.objects.create(
#             checkin=checkin,
#             checkout=checkout,
#             guest=guest,
#             nights=nights,
#             name=name,
#             email=email,
#             phone=phone,
#             requests=requests_text
#         )

#         # redirect to cart page
#         return redirect('cart')  # use the name of your cart url

#     return render(request, 'book.html')

# def contact(request):
#     if request.method == "POST":
#        name=request.POST['name']
#        email=request.POST['email']
#        subject=request.POST['subject']
#        message=request.POST['message']
#        ContactMessage(name=name,email=email,subject=subject,message=message).save()
#        return HttpResponse("Message Sent")


#     return render(request, "contact3.html")
    
# def foot(request):
#     return render(request,'foot.html')

# def room(request):
#     dd=rooms.objects.all()
#     return render(request,'rooms & suits.html',{'dd':dd})


# # def logins(request):
# #     if request.method == "POST":
# #         user_input = request.POST['user']
# #         password = request.POST['password']
# #         from django.contrib.auth.models import User
# #         # Try to find user by username first
# #         user_obj = User.objects.filter(username=user_input).first()
# #         if not user_obj:
# #             # Try to find user by email
# #             user_obj = User.objects.filter(email=user_input).first()
# #         if user_obj:
# #             user = authenticate(username=user_obj.username, password=password)
# #             if user:
# #                 login(request, user)
# #                 return redirect(room)
# #         return HttpResponse("Invalid credentials")
# #     return render(request, 'login.html')

# # def logins(request):
# #     if request.method == "POST":
# #         user_input = request.POST['user']
# #         password = request.POST['password']
# #         from django.contrib.auth.models import User
# #         # Try to find user by username first
# #         user_obj = User.objects.filter(username=user_input).first()
# #         if not user_obj:
# #             # Try to find user by email
# #             user_obj = User.objects.filter(email=user_input).first()
# #         if user_obj:
# #             user = authenticate(username=user_obj.username, password=password)
# #             if user:
# #                 login(request, user)
                
# #                 return redirect(room)
# #         return HttpResponse("Invalid credentials")
# #     return render(request, 'login.html')



# def gallery(request):
#     images = Gallery.objects.all()
#     return render(request,'gallery.html',{'images':images})
# def dinning(request):
#     return render(request,'dinning.html')
# def amantie(request):
#     return render(request,'amantie1.html')
# def daily(request):
#     return render(request,'dailyschedule.html')


# def cart(request,id):
#     if type == 'gallery':
#         item = get_object_or_404(Gallery, id=id)
#     else:
#         item = get_object_or_404(rooms, id=id)

#     total_price = 0
#     ddd = get_object_or_404(rooms, id=id)
#     dd=rooms.objects.all()
#     data = Booking.objects.select_related('room').all()
#     ddd=rooms.objects.get(id=id)
#     # if request.method == 'POST':
#     #     checkin = request.POST['checkin']
#     #     checkout = request.POST['checkout']
#     #     guest = request.POST['guest']
#     #     nights = request.POST['nights']
        

#     #     Booking(checkin=checkin,checkout=checkout,guest=guest,nights=nights).save()
#     #     booking = Booking.objects.create(
#     #           room=ddd,
#     #         checkin=checkin,
#     #         checkout=checkout,
#     #         guest=guest,
#     #         nights=nights
#     #     )
#     if request.method == 'POST':
#         checkin = request.POST['checkin']
#         checkout = request.POST['checkout']
#         guest = int(request.POST['guest'])
#         nights = int(request.POST['nights'])

#         if type == 'gallery':
#             booking = Booking.objects.create(
#                 gallery=item,
#                 checkin=checkin,
#                 checkout=checkout,
#                 guest=guest,
#                 nights=nights
#             )
#             total_price = booking.nights * item.price  # Calculate separately
#         else:
#             booking = Booking.objects.create(
#                 room=item,
#                 checkin=checkin,
#                 checkout=checkout,
#                 guest=guest,
#                 nights=nights
#             )
#             total_price = booking.nights * item.price  # Assuming room has price

#         return redirect('checkout', id=booking.id)

#         # return redirect(checkouts, id=booking.id)
    
#     return render(request, 'cart.html', {'data': data,'dd':dd,'ddd':ddd,'total_price':total_price})


# def roomdetail(request,id):
#     # room = get_object_or_404(Room, id=id)
#     ddd=rooms.objects.get(id=id)
#     if request.method == 'POST':
#         checkin = request.POST['checkin']
#         checkout = request.POST['checkout']
#         guest = request.POST['guest']
#         nights = request.POST['nights']
        

#         # Save booking
#         Booking.objects.create(
#             # room=room,
#             checkin=checkin,
#             checkout=checkout,
#             guest=guest,
#             nights=nights,
           
#         )

#         # Redirect to cart page after booking
#         return redirect(cart)



#     return render(request,'roomdetail.html',{'ddd':ddd})



# from django.shortcuts import render, get_object_or_404
# from .models import Booking, billing  # or Order if you use that for payment

# from .models import Booking, billing

# def bookingconfirm(request, id):
#     booking = get_object_or_404(Booking, id=id)
#     try:
#         bill = billing.objects.get(id=booking.id)
#     except billing.DoesNotExist:
#         bill = None

#     if booking.room:
#         total_price = booking.nights * booking.room.price
#     elif booking.gallery:
#         total_price = booking.nights * booking.gallery.price
#     else:
#         total_price = 0

#     return render(request, "bookingconfirm.html", {
#         "booking": booking,
#         "bill": bill,
#         "total_price": total_price
#     })

# # def bookingconfirm(request, id):
# #     """
# #     Booking confirmation page.
# #     Displays booking details and payment info for the given Order ID.
# #     """
# #     # Fetch the Order using the provided ID
#     # order = get_object_or_404(billing, id=id)

# #     # Ensure we have booking details
# #     booking = order.booking

# #     context = {
# #         "order": billing,
# #         "booking": booking,
# #     }

# #     return render(request, "bookingconfirm.html", context)


# def gallerycart(request, id, type='gallery'):  # type can be 'gallery' or 'room'
#     if type == 'gallery':
#         item = get_object_or_404(Gallery, id=id)
#     else:
#         item = get_object_or_404(rooms, id=id)

#     total_price = 0

#     if request.method == 'POST':
#         checkin = request.POST['checkin']
#         checkout = request.POST['checkout']
#         guest = int(request.POST['guest'])
#         nights = int(request.POST['nights'])

#         if type == 'gallery':
#             booking = Booking.objects.create(
#                 gallery=item,
#                 checkin=checkin,
#                 checkout=checkout,
#                 guest=guest,
#                 nights=nights
#             )
#             total_price = booking.nights * item.price  # Calculate separately
#         else:
#             booking = Booking.objects.create(
#                 room=item,
#                 checkin=checkin,
#                 checkout=checkout,
#                 guest=guest,
#                 nights=nights
#             )
#             total_price = booking.nights * item.price  # Assuming room has price

#         return redirect(reverse('checkout', args=[booking.id]))

#     return render(request, 'gallerycart.html', {'a': item, 'total_price': total_price, 'type': type})


# def checkout(request, id):
#     booking = get_object_or_404(Booking, id=id)

#     if request.method == "POST":
#         # --- Billing Information ---
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         country = request.POST.get("country")

#         # --- Payment Method ---
#         payment_method = request.POST.get("payment_method")
#         card_number = request.POST.get("card_number")
#         expiry_date = request.POST.get("expiry")
#         cvv = request.POST.get("cvv")
#         upi_id = request.POST.get("upi_id")

#         # Update Booking info
#         booking.firstname = first_name
#         booking.lastname = last_name
#         booking.email = email
#         booking.phone = phone
#         booking.country = country
#         booking.save()

#         # Create Billing / Order record
#         bill, created = billing.objects.get_or_create(
#             id=booking.id,  # ensure one-to-one link with booking
#             defaults={
#                 "firstname": first_name,
#                 "lastname": last_name,
#                 "emailaddress": email,
#                 "phone": phone,
#                 "country": country,
#                 "payment_method": payment_method,
#                 "card_number": card_number,
#                 "expiry_date": expiry_date,
#                 "cvv": cvv,
#                 "upi_id": upi_id,
#             }
#         )

#         if not created:
#             # Update existing billing info
#             bill.firstname = first_name
#             bill.lastname = last_name
#             bill.email = email
#             bill.phone = phone
#             bill.country = country
#             bill.payment_method = payment_method
#             bill.card_number = card_number
#             bill.expiry_date = expiry_date
#             bill.cvv = cvv
#             bill.upi_id = upi_id
#             bill.save()

#         # Redirect to booking confirmation
#         return redirect("bookingconfirm", id=booking.id)

#     # --- Calculate total price ---
#     if booking.room:
#         total_price = booking.nights * booking.room.price
#         item_name = booking.room.name
#     elif booking.gallery:
#         total_price = booking.nights * booking.gallery.price
#         item_name = booking.gallery.title
#     else:
#         total_price = 0
#         item_name = "N/A"

#     context = {
#         "booking": booking,
#         "total_price": total_price,
#         "item_name": item_name,
#     }

#     return render(request, "checkout.html", context)


# def forgot(request):
#     if request.method=='POST':
#         email=request.POST['email']
#         user=User.objects.filter(email=email).first()
#         if user:
#             subject='Password Reset Request'
#             reset_link=f'http://127.0.0.1:8000/password_reset/{user.id}/'
#             message=f'Click the link to reset your password: {reset_link}'
#             email_from=settings.EMAIL_HOST_USER
#             recipient_list=[email]
#         try:
#             send_mail(subject,message,email_from,recipient_list)
#             return HttpResponse("Password Reset link sent to your email address")
#         except  Exception as e:
#             return HttpResponse("Email address not found.")
#     return render(request,'forgot_password.html')


# def reset(request,id):
#     user=get_object_or_404(User,id=id)
#     if request.method=='POST':
#         password=request.POST.get('password')
#         cpassword=request.POST.get('cpassword')

#         if password!=cpassword:
#             return HttpResponse("Password do not  match!")
#         user.set_password(password)
#         user.save()

#         return HttpResponse("Password reset successfully")
#         return redirect(logins)
#     return render(request,'password_reset.html',{'user':user})

# # from django.shortcuts import render
# # from app1.models import Room, Booking, GalleryImage, ContactMessage  # adjust model names as needed

# # def dashboard(request):
# #     total_rooms = Room.objects.count()
# #     total_bookings = Booking.objects.count()
# #     total_gallery = GalleryImage.objects.count()
# #     new_messages = ContactMessage.objects.filter(is_read=False).count()

# #     # Example: get 5 most recent activities (customize as needed)
# #     recent_activities = []
# #     for booking in Booking.objects.order_by('-created_at')[:2]:
# #         recent_activities.append(f"Room {booking.room.number} booked by {booking.user.username}")
# #     for img in GalleryImage.objects.order_by('-uploaded_at')[:1]:
# #         recent_activities.append("New gallery image added")
# #     for msg in ContactMessage.objects.order_by('-created_at')[:1]:
# #         recent_activities.append(f"Contact form submitted by {msg.name}")

# #     context = {
# #         'total_rooms': total_rooms,
# #         'total_bookings': total_bookings,
# #         'total_gallery': total_gallery,
# #         'new_messages': new_messages,
# #         'recent_activities': recent_activities,
# #     }
# #     return render(request, 'dashboard.html', context)


# # def dashboard(request):
# #     total_rooms = Room.objects.count() if 'Room' in globals() else 0
# #     total_bookings = Booking.objects.count() if 'Booking' in globals() else 0
# #     total_gallery = GalleryImage.objects.count() if 'GalleryImage' in globals() else 0
# #     new_messages = ContactMessage.objects.filter(is_read=False).count() if 'ContactMessage' in globals() else 0

# #     recent_activities = []
# #     if 'Booking' in globals():
# #         for booking in Booking.objects.order_by('-id')[:2]:
# #             recent_activities.append(f"Room {getattr(booking, 'room', '')} booked by {getattr(getattr(booking, 'user', None), 'username', 'Someone')}")
# #     if 'GalleryImage' in globals():
# #         for img in GalleryImage.objects.order_by('-id')[:1]:
# #             recent_activities.append("New gallery image added")
# #     if 'ContactMessage' in globals():
# #         for msg in ContactMessage.objects.order_by('-id')[:1]:
# #             recent_activities.append(f"Contact form submitted by {getattr(msg, 'name', 'Someone')}")

# #     context = {
# #         'total_rooms': total_rooms,
# #         'total_bookings': total_bookings,
# #         'total_gallery': total_gallery,
# #         'new_messages': new_messages,
# #         'recent_activities': recent_activities,
# #     }
# #     return render(request, 'dashboard.html', context)

# from django.shortcuts import render
# from .models import Room, Booking, Gallery, ContactMessage

# def dashboard(request):

#     total_rooms = Room.objects.count()
#     total_bookings = Booking.objects.count()
#     total_gallery = Gallery.objects.count()
#     new_messages = ContactMessage.objects.count()

#     recent_activities = []
#     for booking in Booking.objects.order_by('-created_at')[:2]:
#         room_name = booking.room.name if booking.room else "Unknown Room"
#         recent_activities.append(f"Room {room_name} booked by {booking.name}")
#     for img in Gallery.objects.order_by('-created_at')[:1]:
#         recent_activities.append("New gallery image added")
#     for msg in ContactMessage.objects.order_by('-created_at')[:1]:
#         recent_activities.append(f"Contact form submitted by {msg.name}")

#     context = {
#         'total_rooms': total_rooms,
#         'total_bookings': total_bookings,
#         'total_gallery': total_gallery,
#         'new_messages': new_messages,
#         'recent_activities': recent_activities,
#     }
#     return render(request, 'dashboard.html', context)


from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.utils import timezone

from .models import Room, Booking, Gallery, ContactMessage, rooms, billing

def index(request):
    return render(request, 'index.html')

def header(request):
    return render(request, 'header.html')

def menu(request):
    return render(request, 'menu2.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phn = request.POST['phn']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=name).exists():
                messages.error(request, 'Username already exists. Please choose another.')
                return render(request, 'register.html')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered. Please use another.')
                return render(request, 'register.html')
            User.objects.create_user(username=name, email=email, password=password).save()
            messages.success(request, 'Registration successful! Please login with your credentials.')
            return redirect('logins')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
            return render(request, 'register.html')
    return render(request, 'register.html')

def book(request, id):
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        guest = request.POST.get('guest')
        nights = request.POST.get('nights')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        requests_text = request.POST.get('requests')
        booking = Booking.objects.create(
            checkin=checkin,
            checkout=checkout,
            guest=guest,
            nights=nights,
            name=name,
            email=email,
            phone=phone,
            requests=requests_text
        )
        return redirect('cart')
    return render(request, 'book.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ContactMessage(name=name, email=email, subject=subject, message=message).save()
        return HttpResponse("Message Sent")
    return render(request, "contact3.html")

def foot(request):
    return render(request, 'foot.html')

def room(request):
    dd = rooms.objects.all()
    return render(request, 'rooms_and_suits.html', {'dd': dd})

def logins(request):
    # If user is already logged in, redirect to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == "POST":
        user_input = request.POST['user']
        password = request.POST['password']
        
        # Try to find user by username or email
        user_obj = User.objects.filter(username=user_input).first()
        if not user_obj:
            user_obj = User.objects.filter(email=user_input).first()
            
        if user_obj:
            user = authenticate(username=user_obj.username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                # Get the next parameter if it exists, otherwise go to dashboard
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
                
        messages.error(request, 'Invalid username/email or password.')
    return render(request, 'login.html')

def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})

def dinning(request):
    return render(request, 'dinning.html')

def amantie(request):
    return render(request, 'amantie1.html')

def daily(request):
    return render(request, 'dailyschedule.html')

@login_required(login_url='/logins')
def cart(request, id):
    item = get_object_or_404(rooms, id=id)
    total_price = 0
    ddd = get_object_or_404(rooms, id=id)
    dd = rooms.objects.all()
    data = Booking.objects.select_related('room').filter(room=item)
    if request.method == 'POST':
        # Use safe accessors to avoid MultiValueDictKeyError when fields are missing
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        guest = int(request.POST.get('guest') or 1)
        nights_raw = request.POST.get('nights')

        # Calculate nights: prefer provided 'nights' if valid, otherwise derive from dates
        actual_nights = None
        from datetime import datetime
        if nights_raw:
            try:
                actual_nights = int(nights_raw)
            except (ValueError, TypeError):
                actual_nights = None

        if actual_nights is None and checkin and checkout:
            try:
                checkin_date = datetime.strptime(checkin, '%Y-%m-%d').date()
                checkout_date = datetime.strptime(checkout, '%Y-%m-%d').date()
                actual_nights = max(0, (checkout_date - checkin_date).days)
            except Exception:
                actual_nights = 0

        if actual_nights is None:
            actual_nights = 0

        booking = Booking.objects.create(
            room=item,
            checkin=checkin,
            checkout=checkout,
            guest=guest,
            nights=actual_nights,
            name=request.user.get_full_name() or request.user.username,
            email=request.user.email
        )
        total_price = booking.nights * item.price
        return redirect('checkout', id=booking.id)
    return render(request, 'cart.html', {'data': data, 'dd': dd, 'ddd': ddd, 'total_price': total_price})

def roomdetail(request, id):
    ddd = rooms.objects.get(id=id)
    if request.method == 'POST':
        # Use safe accessors and compute nights server-side
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        guest = int(request.POST.get('guest') or 1)
        nights_raw = request.POST.get('nights')

        actual_nights = None
        from datetime import datetime
        if nights_raw:
            try:
                actual_nights = int(nights_raw)
            except (ValueError, TypeError):
                actual_nights = None

        if actual_nights is None and checkin and checkout:
            try:
                checkin_date = datetime.strptime(checkin, '%Y-%m-%d').date()
                checkout_date = datetime.strptime(checkout, '%Y-%m-%d').date()
                actual_nights = max(0, (checkout_date - checkin_date).days)
            except Exception:
                actual_nights = 0

        if actual_nights is None:
            actual_nights = 0

        Booking.objects.create(
            checkin=checkin,
            checkout=checkout,
            guest=guest,
            nights=actual_nights,
        )
        return redirect(cart)
    return render(request, 'roomdetail.html', {'ddd': ddd})

# def bookingconfirm(request, id):
#     booking = get_object_or_404(Booking, id=id)
#     try:
#         bill = billing.objects.get(id=booking.id)
#     except billing.DoesNotExist:
#         bill = None
    
#     # Recalculate nights based on actual check-in and check-out dates
#     if booking.checkin and booking.checkout:
#         delta = booking.checkout - booking.checkin
#         actual_nights = delta.days
#     else:
#         actual_nights = booking.nights
    
#     if booking.room:
#         total_price = actual_nights * booking.room.price
#     elif hasattr(booking, 'gallery') and booking.gallery:
#         total_price = actual_nights * booking.gallery.price
#     else:
#         total_price = 0
    
#     # Update the booking with the calculated nights
#     booking.nights = actual_nights
#     booking.save()
    
#     return render(request, "bookingconfirm.html", {
#         "booking": booking,
#         "bill": bill,
#         "total_price": total_price
#     })
def bookingconfirm(request, id):
    booking = get_object_or_404(Booking, id=id)

    try:
        bill = billing.objects.get(booking=booking)
    except billing.DoesNotExist:
        bill = None

    total_price = 0
    if booking.room:
        total_price = booking.room.price * booking.nights
    elif booking.gallery:
        total_price = booking.gallery.price * booking.nights  # Only if gallery includes price

    return render(request, "bookingconfirm.html", {
        "booking": booking,
        "bill": bill,
        "total_price": total_price,
    })

# def bookingconfirm(request, id):
#     booking = get_object_or_404(Booking, id=id)

#     # Safety lookup for bill
#     try:
#         bill = billing.objects.get(booking=booking)
#     except billing.DoesNotExist:
#         bill = None

#     total_price = 0
#     if booking.room:
#         total_price = booking.room.price * booking.nights

#     return render(request, "bookingconfirm.html", {
#         "booking": booking,
#         "bill": bill,
#         "total_price": total_price,
#     })

def gallerycart(request, id, type='gallery'):
    if type == 'gallery':
        item = get_object_or_404(Gallery, id=id)
    else:
        item = get_object_or_404(rooms, id=id)
    total_price = 0
    if request.method == 'POST':
        # Safe POST access and compute nights server-side
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        guest = int(request.POST.get('guest') or 1)
        nights_raw = request.POST.get('nights')

        actual_nights = None
        from datetime import datetime
        if nights_raw:
            try:
                actual_nights = int(nights_raw)
            except (ValueError, TypeError):
                actual_nights = None

        if actual_nights is None and checkin and checkout:
            try:
                checkin_date = datetime.strptime(checkin, '%Y-%m-%d').date()
                checkout_date = datetime.strptime(checkout, '%Y-%m-%d').date()
                actual_nights = max(0, (checkout_date - checkin_date).days)
            except Exception:
                actual_nights = 0

        if actual_nights is None:
            actual_nights = 0

        if type == 'gallery':
            booking = Booking.objects.create(
                gallery=item,
                checkin=checkin,
                checkout=checkout,
                guest=guest,
                nights=actual_nights
            )
            total_price = booking.nights * item.price
        else:
            booking = Booking.objects.create(
                room=item,
                checkin=checkin,
                checkout=checkout,
                guest=guest,
                nights=actual_nights
            )
            total_price = booking.nights * item.price
        return redirect(reverse('checkout', args=[booking.id]))
    return render(request, 'gallerycart.html', {'a': item, 'total_price': total_price, 'type': type})

def checkout(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("country")
        payment_method = request.POST.get("payment_method")
        card_number = request.POST.get("card_number")
        expiry_date = request.POST.get("expiry")
        cvv = request.POST.get("cvv")
        upi_id = request.POST.get("upi_id")
        booking.firstname = first_name
        booking.lastname = last_name
        booking.email = email
        booking.phone = phone
        booking.country = country
        booking.save()
        bill, created = billing.objects.get_or_create(
            id=booking.id,
            defaults={
                "firstname": first_name,
                "lastname": last_name,
                "emailaddress": email,
                "phone": phone,
                "country": country,
                "payment_method": payment_method,
                "card_number": card_number,
                "expiry_date": expiry_date,
                "cvv": cvv,
                "upi_id": upi_id,
            }
        )
        if not created:
            bill.firstname = first_name
            bill.lastname = last_name
            bill.email = email
            bill.phone = phone
            bill.country = country
            bill.payment_method = payment_method
            bill.card_number = card_number
            bill.expiry_date = expiry_date
            bill.cvv = cvv
            bill.upi_id = upi_id
            bill.save()
        return redirect("bookingconfirm", id=booking.id)
    if booking.room:
        total_price = booking.nights * booking.room.price
        item_name = booking.room.name
    elif hasattr(booking, 'gallery') and booking.gallery:
        total_price = booking.nights * booking.gallery.price
        item_name = booking.gallery.title
    else:
        total_price = 0
        item_name = "N/A"
    context = {
        "booking": booking,
        "total_price": total_price,
        "item_name": item_name,
    }
    return render(request, "checkout.html", context)

# def test_email(request):
#     try:
#         # Test settings configuration
#         if not django_settings.EMAIL_HOST_USER:
#             return HttpResponse("Error: EMAIL_HOST_USER is not set in settings.py")
#         if not django_settings.EMAIL_HOST_PASSWORD:
#             return HttpResponse("Error: EMAIL_HOST_PASSWORD is not set in settings.py")
        
#         # Try to send test email
#         subject = 'Test Email from Raj Vilas Palace'
#         message = 'This is a test email from your Django application.'
#         from_email = django_settings.DEFAULT_FROM_EMAIL
#         recipient_list = [django_settings.EMAIL_HOST_USER]
        
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
#             f"Using backend: {django_settings.EMAIL_BACKEND}"
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

def forgot(request):
    message = None
    message_type = None
    
    # DEBUG: Check what 'settings' actually is
    print(f"DEBUG: Type of settings: {type(settings)}")
    print(f"DEBUG: Is settings the Django settings? {hasattr(settings, 'DEBUG')}")
    
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            message = "Please enter an email address."
            message_type = "error"
        else:
            user = User.objects.filter(email=email).first()
            
            if user:
                try:
                    # DEBUG: Check before using settings
                    print(f"DEBUG: DEFAULT_FROM_EMAIL exists? {hasattr(settings, 'DEFAULT_FROM_EMAIL')}")
                    
                    # Use the CORRECT settings import
                    from django.conf import settings as django_settings
                    
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
                    
                    # HTML version (your existing HTML code here)
                    html_message = f'''
                    <!-- Your HTML email template here -->
                    '''
                    
                    # Use django_settings instead of settings
                    msg = EmailMultiAlternatives(
                        subject,
                        text_message,
                        django_settings.DEFAULT_FROM_EMAIL,  # FIXED: Use django_settings
                        [email]
                    )
                    msg.attach_alternative(html_message, "text/html")
                    msg.send()
                    
                    message = "✅ Password reset link has been sent to your email address!"
                    message_type = "success"
                    print(f"EMAIL SENT SUCCESSFULLY!")
                    
                except Exception as e:
                    print(f"EMAIL SENDING FAILED: {e}")
                    import traceback
                    print(f"Full traceback: {traceback.format_exc()}")
                    message = f"❌ Failed to send email. Error: {str(e)}"
                    message_type = "error"
            else:
                message = "❌ Email address not found in our system."
                message_type = "error"
    
    return render(request, 'forgot_password.html', {'message': message, 'message_type': message_type})
def reset(request, id):
    user = get_object_or_404(User, id=id)
    error_message = None
    
    if request.method == 'POST':
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            error_message = "Passwords do not match!"
        elif len(password) < 6:
            error_message = "Password must be at least 6 characters long!"
        else:
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successfully! Please login with your new password.')
            return redirect('logins')  # Redirect to login page
    
    context = {
        'user': user,
        'error': error_message
    }
    return render(request, 'password_reset.html', context)

from django.contrib.auth import logout

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
    return redirect('index')

@login_required(login_url='/logins')
def dashboard(request):
    # Get total counts from both Room and rooms models
    total_rooms = rooms.objects.count()
    total_bookings = Booking.objects.count()
    total_gallery = Gallery.objects.count()
    new_messages = ContactMessage.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7)).count()
    
    # Get notification count for the badge
    notifications_count = (
        Booking.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7)).count() +
        ContactMessage.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7)).count()
    )
    
    # Get recent activities with proper timestamps
    recent_activities = []
    
    # Get recent bookings
    recent_bookings = Booking.objects.order_by('-created_at')[:3]
    for booking in recent_bookings:
        room_info = ""
        if booking.room:
            room_info = f"Room {booking.room.name}"
        elif booking.gallery:
            room_info = f"Room {booking.gallery.title}"
        else:
            room_info = "Room"
            
        recent_activities.append({
            'text': f"{room_info} booked by {booking.name if booking.name else 'Guest'}",
            'time': booking.created_at,
            'icon': 'fa-calendar-check'
        })
    
    # Get recent gallery additions
    recent_images = Gallery.objects.order_by('-created_at')[:2]
    for img in recent_images:
        recent_activities.append({
            'text': f"New gallery image added: {img.title or 'Untitled'}",
            'time': img.created_at,
            'icon': 'fa-image'
        })
    
    # Get recent messages
    recent_messages = ContactMessage.objects.order_by('-created_at')[:2]
    for msg in recent_messages:
        recent_activities.append({
            'text': f"New message from {msg.name}: {msg.subject or 'No subject'}",
            'time': msg.created_at,
            'icon': 'fa-envelope'
        })
    
    # Sort activities by time
    recent_activities.sort(key=lambda x: x['time'], reverse=True)
    
    # Convert timestamps to "time ago" format
    for activity in recent_activities:
        time_diff = timezone.now() - activity['time']
        if time_diff.days > 0:
            activity['time_ago'] = f"{time_diff.days}d ago"
        elif time_diff.seconds >= 3600:
            activity['time_ago'] = f"{time_diff.seconds // 3600}h ago"
        elif time_diff.seconds >= 60:
            activity['time_ago'] = f"{time_diff.seconds // 60}m ago"
        else:
            activity['time_ago'] = "Just now"
    
    # Limit to most recent 5 activities
    recent_activities = recent_activities[:5]
    
    context = {
        'total_rooms': total_rooms,
        'total_bookings': total_bookings,
        'total_gallery': total_gallery,
        'new_messages': new_messages,
        'recent_activities': recent_activities,
        'unread_notifications_count': notifications_count
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='/logins')
def notifications(request):
    # Get recent notifications
    notifications = []
    unread_count = 0
    
    # Add booking notifications
    recent_bookings = Booking.objects.order_by('-created_at')[:5]
    for booking in recent_bookings:
        room_info = ""
        if booking.room:
            room_info = booking.room.name
        elif booking.gallery:
            room_info = booking.gallery.title
        else:
            room_info = "Unknown Room"
            
        notifications.append({
            'title': 'New Booking',
            'message': f"Booking received from {booking.name if booking.name else 'Guest'} for {room_info}",
            'details': f"Duration: {booking.nights} nights",
            'time': booking.created_at,
            'type': 'success',
            'icon': 'fa-calendar-check'
        })
        unread_count += 1
    
    # Add message notifications
    recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
    for msg in recent_messages:
        notifications.append({
            'message': f"New message from {msg.name}: {msg.subject or 'No subject'}",
            'time': msg.created_at,
            'type': 'info',
            'icon': 'fa-envelope'
        })
        unread_count += 1
    
    # Sort notifications by time
    notifications.sort(key=lambda x: x['time'], reverse=True)
    
    # Convert timestamps to "time ago" format
    for notification in notifications:
        time_diff = timezone.now() - notification['time']
        if time_diff.days > 0:
            notification['time_ago'] = f"{time_diff.days}d ago"
        elif time_diff.seconds >= 3600:
            notification['time_ago'] = f"{time_diff.seconds // 3600}h ago"
        elif time_diff.seconds >= 60:
            notification['time_ago'] = f"{time_diff.seconds // 60}m ago"
        else:
            notification['time_ago'] = "Just now"
    
    context = {
        'notifications': notifications,
        'unread_notifications_count': unread_count
    }
    return render(request, 'notifications.html', context)

@login_required(login_url='/logins')
def settings(request):
    if request.method == 'POST':
        # Handle settings updates here
        messages.success(request, 'Settings updated successfully!')
        return redirect('settings')
    
    context = {
        'user': request.user,
        'settings_sections': [
            {
                'title': 'Profile Settings',
                'icon': 'fa-user',
                'settings': [
                    {'name': 'name', 'label': 'Full Name', 'type': 'text', 'value': request.user.get_full_name()},
                    {'name': 'email', 'label': 'Email', 'type': 'email', 'value': request.user.email}
                ]
            },
            {
                'title': 'Notification Preferences',
                'icon': 'fa-bell',
                'settings': [
                    {'name': 'email_notifications', 'label': 'Email Notifications', 'type': 'checkbox', 'value': True},
                    {'name': 'booking_alerts', 'label': 'Booking Alerts', 'type': 'checkbox', 'value': True}
                ]
            },
            {
                'title': 'Security',
                'icon': 'fa-lock',
                'settings': [
                    {'name': 'change_password', 'label': 'Change Password', 'type': 'button', 'action': 'change_password'}
                ]
            }
        ]
    }
    return render(request, 'settings.html', context)