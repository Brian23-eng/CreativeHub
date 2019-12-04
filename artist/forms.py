from django import forms
from . models import Profile, Comments, Post

class PostImagesForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date']


class PostComments(forms.ModelForm):
    class Meta: 
        model = Comments
        exclude = ['image','posted','user']
        
class PostProfile(forms.ModelForm):
    class Meta:
        models = Profile
        exclude = ['user',]

    