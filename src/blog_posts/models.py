from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """Declare fields that will be mapped into the database."""
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
