# Generated by Django 2.2 on 2020-09-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0004_auto_20200924_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
