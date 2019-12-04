from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_picure = models.ImageField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    contact = models.IntegerField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    
class Post(models.Model):
    title: models.CharField(blank=False, max_length=500)
    ig_url= models.CharField(max_length=100, blank=True)
    description =models.TextField(max_length=500, blank=False)
    photo = models.ImageField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateField(auto_now_add=True, blank=True)
    
class Comments(models.Model):
    comment = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)