# Generated by Django 2.2 on 2020-09-25 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0006_blogpost_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
