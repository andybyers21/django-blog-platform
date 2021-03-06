"""django_blog_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .views import (about_page,
                    contact_page,
                    home_page
                    )

from search.views import search_view
from blog_posts.views import (blog_post_create_view)


urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('admin/', admin.site.urls),
    path('blog/', include('blog_posts.urls')),
    path('contact/', contact_page),
    path('create/', blog_post_create_view),
    path('search/', search_view)
]

if settings.DEBUG:
    """ Test/ Debug area for serving static files """
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
