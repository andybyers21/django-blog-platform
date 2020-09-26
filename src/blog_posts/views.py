# from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm


def blog_post_list_view(request):
    # return a list of objects (blog posts)
    # search?

    # qs = query set list view, .published for search feature to only get the published posts
    qs = BlogPost.objects.all().published()

    # show draft posts to authenticated user
    if request.user.is_authenticated:
        user_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | user_qs).distinct()

    template_name = "blog_posts/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


# @login_required
@staff_member_required
def blog_post_create_view(request):
    # create objects with a django form
    # request.user will return something...
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        form.save()
        form = BlogPostModelForm()
    template_name = "form.html"
    context = {"form": form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # return single object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


# @login_required
@staff_member_required
# TODO: add redirect after form.save
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog_posts/form.html'
    context = {"form": form, "title": f"Updating: {obj.title}"}
    return render(request, template_name, context)
    # TODO: add date format YYYY-MM-DD to update page


# @login_required
@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_posts/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {"object": obj}
    return render(request, template_name, context)
