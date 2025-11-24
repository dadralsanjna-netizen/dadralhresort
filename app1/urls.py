from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from . import views
from . import fixed_views
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('header', header, name='header'),
    path('menu', menu, name='menu'),
    path('register', register, name='register'),
    path('book/<int:id>', book, name='book'),
    path('contact', contact, name='contact'),
    path('foot', foot, name='foot'),
    path('gallery', gallery, name='gallery'),
    path('logins', logins, name='logins'),
    path('rooms', views.room, name='room'),
    path('dinning', dinning, name='dinning'),
    path('amantie', amantie, name='amantie'),
    path('daily', daily, name='daily'),
    path('cart/<int:id>/', cart, name='cart'),
    path('cart/<int:id>', cart),  # Fallback for no trailing slash
    # path('bookingconfirm/<int:id>/', views.bookingconfirm, name='bookingconfirm'),
    # path('bookingconfirm/<int:id>/', views.bookingconfirm, name='bookingconfirm'),
    path('bookingconfirm/<int:id>/', views.bookingconfirm, name='bookingconfirm'),

    path('roomdetail/<int:id>/', roomdetail, name='roomdetail'),
    path('gallerycart/<int:id>/', gallerycart, name='gallerycart'),
    path('checkouts/<int:id>/', views.checkout, name='checkout'),
    path('password_reset/<int:id>/', views.reset, name='reset'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings, name='settings'),
    path('forgot/', views.forgot, name='forgot'),
]