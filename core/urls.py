"""
URL patterns for the core app.

This module defines the URL patterns for the core app, which is responsible for handling requests related to landing,
index, about, pricing, review, contact, signup, login, and logout.

The urlpatterns list maps URL patterns to corresponding views and names.
The views are imported from the .views module, and the LoginView and LogoutView
classes are imported from the django.contrib.auth.views module.
The LoginForm is imported from the .forms module.
"""

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
]

