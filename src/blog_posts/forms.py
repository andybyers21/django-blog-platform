from django import forms

from .models import BlogPost


# class BlogPostForm(forms.Form):
#     # I think this is redundant codez
#     title = forms.CharField()
#     slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title',
                  'image',
                  'slug',
                  'content',
                  'publish_date']

    # def clean_title(self, *args, **kwargs):
    #     """ Prevent duplicate title instances.

    #     This code is not working and I don't know why???
    #     Look up and make your own.
    #     """
    #     instance = self.instance
    #     title = self.cleaned_data.get('title')
    #     qs = BlogPost.objects.filter(title__iexact=title)
    #     if instance is not None:
    #         qs = qs.exclude(pk=instance.pk)     # id=instance.id
    #     if qs.exists:
    #         raise forms.ValidationError(
    #             "This title has already been used. Please choose another.")
    #     return title
