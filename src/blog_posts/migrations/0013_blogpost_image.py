# Generated by Django 2.2 on 2020-09-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0012_auto_20200926_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
