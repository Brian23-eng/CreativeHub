from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


def home(request):
    title = 'Creative || Hub'
    
    return render(request, 'index.html',{'title': title})

@login_required(login_url='login')
def photos(request):
    posts = Post.all_posts()
    return render(request, 'photo.html',{'posts':posts})


