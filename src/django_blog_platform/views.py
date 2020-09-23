# from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    username = request.user.username
    hometitle = f"Welcome to my django-blog-platform " + username
    return render(request, 'home.html', {"title": hometitle})


def about_page(request):
    return render(request, 'about.html', {"title": "About Me"})


def contact_page(request):
    return render(request, 'contact.html', {"title": "Contact Me"})
