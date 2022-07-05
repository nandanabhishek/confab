# Generated by Django 4.0.1 on 2022-01-30 05:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_room_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='room_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]