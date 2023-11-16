"""
Module for item views.

This module defines the following view functions:
- items: Renders the items page with a list of items based on the request parameters.
- detail: Renders the detail page for a specific item.
- new: Renders the new item form page and handles form submission to create a new item.
- edit: Renders the edit item form page and handles form submission to edit an existing item.
- delete: Deletes an item and redirects to the dashboard index page.
"""

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Category, Item

def items(request):
    """
     Renders the items page with a list of items based on the request parameters.
    Parameters:
        - request: The HTTP request object.
    Returns:
        - The rendered items.html template with the items, query, categories,
        and category_id context variables.
    """
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    """
     Renders the detail page for a specific item.
    Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the item.
    Returns:
        - The rendered detail.html template with the item and related_items context variables.
    """
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    """
     Renders the new item form page and handles form submission to create a new item.
    Parameters:
        - request: The HTTP request object.
    Returns:
        - If the request method is POST and the form is valid,
        redirects to the item detail page for the new item.
        - If the request method is not POST, renders the form.html
        template with the new item form and title context variables.
    """
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    """
     Renders the edit item form page and handles form submission to edit an existing item.
    Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the item.
    Returns:
        - If the request method is POST and the form is valid, redirects to
        the item detail page for the edited item.
        - If the request method is not POST, renders the form.html template with
        the edit item form and title context variables.
    """
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    """
     Deletes an item specified by its primary key and the authenticated user.
    Parameters:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the item to be deleted.
    Returns:
        HttpResponseRedirect: A redirect response to the index page of the dashboard.
    """
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')