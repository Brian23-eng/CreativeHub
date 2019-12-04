from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from . forms import PostComments, PostImagesForm,PostProfile


def home(request):
    title = 'Creative || Hub'
    
    return render(request, 'index.html',{'title': title})

@login_required(login_url='login')
def photos(request):
    posts = Post.all_posts()
    return render(request, 'photo.html',{'posts':posts})

def post_image(request):
    if request.method == 'POST':
        form = PostImagesForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
    else:
        form = PostImagesForm()
        
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None
    return rebder(request,'post_image.html',{'posts': posts, 'forms':forms})


