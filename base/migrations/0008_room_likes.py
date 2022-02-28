# Generated by Django 4.0.1 on 2022-01-29 19:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_user_url_fb_alter_user_url_git_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='likes',
            field=models.ManyToManyField(related_name='room_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
