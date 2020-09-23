from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    username = request.user.username
    hometitle = f"Welcome to my django-blog-platform " + username
    context = {"title": hometitle, "aList": [
        "one", "two", "three", "four", "five"]}
    return render(request, 'home.html', context)


def about_page(request):
    return render(request, 'about.html', {"title": "About Me"})


def contact_page(request):
    return render(request, 'contact.html', {"title": "Contact Me"})
