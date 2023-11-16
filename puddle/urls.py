"""
Module for URL configuration.

This module defines the URL patterns for the project.

The urlpatterns list contains the following URL patterns:

- '': Includes the URL patterns defined in the 'core.urls' module.
- 'items/': Includes the URL patterns defined in the 'item.urls' module.
- 'dashboard/': Includes the URL patterns defined in the 'dashboard.urls' module.
- 'inbox/': Includes the URL patterns defined in the 'conversation.urls' module.
- 'admin/': Includes the default Django admin site URL patterns.

It also includes static URL patterns for serving media files.

The 'MEDIA_URL' and 'MEDIA_ROOT' settings from 'django.conf.settings' are used to define the static URL patterns.

Returns:
    - The urlpatterns list that defines the URL patterns for the project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# puddle/urls.py

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)