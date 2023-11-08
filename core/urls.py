from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
