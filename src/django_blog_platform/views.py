from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog_posts.models import BlogPost


def home_page(request):
    username = request.user.username
    hometitle = f"Welcome to my django-blog-platform " + username
    qs = BlogPost.objects.all()[:5]
    context = {"title": hometitle, 'blog_list': qs}
    return render(request, 'home.html', context)


def about_page(request):
    return render(request, 'about.html', {"title": "About Me"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact ME",
               "form": form}
    return render(request, 'form.html', context)
