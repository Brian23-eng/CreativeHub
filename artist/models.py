from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_picure = models.ImageField(blank=True)
    bio = models.TextField(max_length=500, blank=True)
    contact = models.IntegerField(blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

