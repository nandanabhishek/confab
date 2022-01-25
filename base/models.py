from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    
    url_fb = models.URLField(null=True, blank=True, verbose_name='Url-Facebook')
    url_insta = models.URLField(null=True, blank=True, verbose_name='Url-Instagram')
    # url_twitter = models.URLField(null=True, blank=False, verbose_name='Url-Twitter')
    url_linkedin = models.URLField(null=True, blank=True, verbose_name='Url-Linkedin')
    url_git = models.URLField(null=True, blank=True, verbose_name='Url-GitHub')
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200)
    
    # null-True means this field can be null in database
    # blank-True means this field can be null/empty when we submit the form
    description = models.TextField(null=True, blank=True)
    
    # this fiels will store all the users currently in the room
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    
    # this is meant to give a timestamp, when we save our model
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    # difference b/w auto_now and auto_now_add :
    # auto_now takes snapshot everytime we save an item
    # auto_now_add takes snapshot only once we save it for the first time.
    
    # will add an option to like room
    # like
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # here message needs to be many to one relationship
    # with room, i.e for 1 room we can have n messages
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    
    # will allow to share pdf and images in room as well in room body
    
    # this is meant to give a timestamp, when we save our model
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
     
    def __str__(self) -> str:
        return self.body[0:50]
