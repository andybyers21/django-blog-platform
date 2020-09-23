from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'hello_world.html', {"title": "django-blog-platform"})


def about_page(request):
    return render(request, 'hello_world.html', {"title": "About Me"})


def contact_page(request):
    return render(request, 'hello_world.html', {"title": "Contact Me"})
