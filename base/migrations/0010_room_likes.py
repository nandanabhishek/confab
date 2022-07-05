# Generated by Django 4.0.1 on 2022-01-30 05:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_room_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='likes',
            field=models.ManyToManyField(related_name='room_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]