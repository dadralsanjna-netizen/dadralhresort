from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # time

class UserRegistration(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)  # store hashed password later
    created_at = models.DateTimeField(auto_now_add=True)





    

class rooms(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='images/')




class Room(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # per night
    max_adults = models.PositiveIntegerField(default=2)
    max_children = models.PositiveIntegerField(default=2)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name



class Gallery(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="gallery", null=True, blank=True)

    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"
    # class Booking(models.Model):
    #     room = models.ForeignKey(rooms, on_delete=models.CASCADE, null=True, blank=True)
    # gallery = models.ForeignKey(Gallery, null=True, blank=True, on_delete=models.CASCADE)
    # checkin = models.DateField()
    # checkout = models.DateField()
    # guest = models.PositiveIntegerField()
    # nights = models.PositiveIntegerField()
    # name = models.CharField(max_length=150)
    # email = models.EmailField()
    # phone = models.CharField(max_length=20)
    # country = models.CharField(max_length=50, blank=True)
    # requests = models.TextField(blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.name} ({self.id})"

class Booking(models.Model):
    room = models.ForeignKey(rooms, on_delete=models.CASCADE, null=True, blank=True)
    gallery = models.ForeignKey(Gallery, null=True, blank=True, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    guest = models.PositiveIntegerField()
    nights = models.PositiveIntegerField()
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50, blank=True)
    requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.id})"
   
# class Booking(models.Model):
#     room = models.ForeignKey(rooms, on_delete=models.CASCADE,null=True, blank=True)
#     gallery = models.ForeignKey(Gallery, null=True, blank=True, on_delete=models.CASCADE)
#     checkin = models.DateField()
#     checkout = models.DateField()
#     guest = models.PositiveIntegerField()
#     nights = models.PositiveIntegerField()
#     name = models.CharField(max_length=150)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     country=models.CharField(max_length=50,blank=True)
#     requests = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        if self.room:
            return self.nights * self.room.price
        return 0

    def __str__(self):
        return f"Booking by {self.name} ({self.checkin} → {self.checkout})"


# class cartitem(models.Model):
class A(models.Model):
    room = models.ForeignKey("rooms", on_delete=models.CASCADE, null=True, blank=True)  
    gallery = models.ForeignKey(Gallery, null=True, blank=True, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    guest = models.PositiveIntegerField()
    nights = models.PositiveIntegerField()

    def total_price(self):
        if self.room:
            return self.nights * self.room.price
        return 0


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class billing(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('upi', 'UPI'),
        ('credit_card', 'Credit Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    # Billing info
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    emailaddress = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    # Address fields (optional)
    address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)

    # Payment
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        default='cod'
    )
    card_number = models.CharField(max_length=20, blank=True, null=True)
    expiry_date = models.CharField(max_length=10, blank=True, null=True)
    cvv = models.CharField(max_length=5, blank=True, null=True)
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)  

    # Totals
    line_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order #{self.id} - {self.firstname or ''} {self.lastname or ''}"

