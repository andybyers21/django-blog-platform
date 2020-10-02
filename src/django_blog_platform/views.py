from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog_posts.models import BlogPost
from blog_posts.forms import BlogPostModelForm


def home_page(request):
    username = request.user.username
    hometitle = f"Welcome to this django-blog-platform " + username
    qs = BlogPost.objects.all().published()[:5]
    context = {"title": hometitle, 'blog_list': qs}
    return render(request, 'home.html', context)


def about_page(request):
    hometitle = f"About Us"
    return render(request, 'about.html', {"title": hometitle})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact US",
               "form": form}
    return render(request, 'form.html', context)
