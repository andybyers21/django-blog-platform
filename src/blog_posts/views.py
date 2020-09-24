from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost


def blog_post_list_view(request):
    # return a list of objects (blog posts)
    # search?
    qs = BlogPost.objects.all()     # list view
    template_name = "blog_posts/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # create objects with a django form
    template_name = "blog_posts/create.html"
    context = {"form": None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # return single object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/update.html'
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)
