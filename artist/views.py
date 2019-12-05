from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from . forms import PostComments, PostImagesForm,PostProfile
from django.contrib.auth.models import User


def home(request):
    title = 'Creative || Hub'
    
    return render(request, 'index.html',{'title': title})

@login_required(login_url='login')
def photos(request):
    posts = Post.all_posts()
    return render(request, 'photo.html',{'posts':posts})


@login_required(login_url='login')
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
    return render(request,'post_image.html',{'posts': posts, 'form':form})

def edit_profile(request, username):
    user = User.objetcs.get(username=username)
    if request.method == 'POST':
        user_form = PostProfile(instance=request.user)
        prof_form = PostProfile(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.user_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
        
    else:
        user_form = PostProfile(instance=request.user)
        prof_form = PostProfile(instance=request.user.profile)
        
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    
    return render(request, 'edit.html', params)


def profile(request, username):
    return render(request, 'profile.html')

def single_art(request, art_id):
    try:
        arts = Post.objects.get(id=art_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'single_art.html',{'arts':arts})
        
    



