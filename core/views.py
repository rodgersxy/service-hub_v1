"""
This module provides views for the core application.
"""

from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    """
    This function handles the index page.
    
    :param request: The HTTP request object.
    :return: The rendered index page with categories and items.
    """
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def landing(request):
    """
    This function handles the landing page.
    
    :param request: The HTTP request object.
    :return: The rendered landing page.
    """
    return render(request, 'core/landing.html')

def contact(request):
    """
    This function handles the contact page.
    
    :param request: The HTTP request object.
    :return: The rendered contact page.
    """
    return render(request, 'core/contact.html')

def about(request):
    """
    This function handles the about page.
    
    :param request: The HTTP request object.
    :return: The rendered about page.
    """
    return render(request, 'core/about.html')

def pricing(request):
    """
    This function handles the pricing page.
    
    :param request: The HTTP request object.
    :return: The rendered pricing page.
    """
    return render(request, 'core/pricing.html')

def review(request):
    """
     This function handles the review page.
    
    :param request: The HTTP request object.
    :return: The rendered review page.
    """
    return render(request, 'core/review.html')

def signup(request):
    """
    This function handles the signup page.
    
    :param request: The HTTP request object.
    :return: The rendered signup page with the signup form.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout(request):
    """
    This function handles the logout page.
    
    :param request: The HTTP request object.
    :return: The rendered logout page.
    """
    return render(request, 'core/logout.html')