"""
This module provide the view for the dashboard application
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item

@login_required
def index(request):
    """
    Renders the 'dashboard/index.html' template with a context containing the items created by the logged-in user.
    Parameters:
        request (HttpRequest): The HTTP request object sent by the client.
    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })
