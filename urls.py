"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs',views.aboutUs, name='aboutUs'),
    path('menu',views.menu, name='menu'),
    path('events',views.events, name='events'),
    path('gallery',views.gallery, name='gallery'),
    path('contact',views.contact, name='contact'),
    path('reservation',views.reservation, name='reservation'),
    path('login',views.login, name='login'),
    path('forget_password',views.forget_password, name='forget_password'),
    path('logout',views.logout, name='logout'),
    path('confirm_password',views.confirm_password, name='confirm_password'),
    path('registration',views.registration, name='registration'),
    path('order',views.order, name='order'),
    path('shop_detail/<int:id>',views.shop_detail, name='shop_detail'),
    path('category/<int:id>',views.category, name='category'),
    path('shopping_cart',views.shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:id>',views.add_to_cart, name='add_to_cart'),
    path('plus/<int:id>', views.plus, name='plus'),
    path('minus/<int:id>', views.minus, name='minus'),
    path('remove/<int:id>',views.remove, name='remove'),
    path('billing_address',views.billing_address, name='billing_address'),
    path('checkout', views.checkout, name='checkout'),
    path('wishlist',views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:id>',views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist_remove/<int:id>',views.wishlist_remove, name='wishlist_remove'),
    path('change_address',views.change_address, name='change_address'),
    path('payload', views.payload, name='payload'),
    path('error',views.error, name='error'),
    path('my_address',views.my_address, name='my_address'),

]
