# Generated by Django 4.0.1 on 2022-01-30 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_room_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='likes',
        ),
    ]
