from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from . models import Post, Profile, Comments
from . forms import PostComments, PostImagesForm,PostProfile
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
from friendship.exceptions import AlreadyExistsError



def home(request):
    title = 'Creative || Hub'
    
    return render(request, 'index.html',{'title': title})

@login_required(login_url='login')
def photos(request):
    title = 'Creative || Hub'
    posts = Post.objects.all()
    return render(request,'photo.html',{'posts':posts , 'title':title})


@login_required(login_url='login')
def post_image(request):
    title = 'Creative || Hub'
    if request.method == 'POST':
        form = PostImagesForm(request.POST,request.FILES)
        
        # photo = f'images/{request.POST["photo"]}'
        print(form)
        print(request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(photos)
            
    else:
        form = PostImagesForm()
        print('method is not post')
        
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None
    return render(request,'post_image.html',{'posts': posts, 'form':form, 'title':title})

def edit_profile(request, username):
    title = 'Creative || Hub'
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
        'prof_form': prof_form,
        'title':title
    }
    
    return render(request, 'edit.html', params)


def profile(request, username):
    title = 'Creative || Hub'
    profile = User.objects.get(username=username)
    users = User.objects.get(username=username)
    follow = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    people_following = Follow.objects.following(request.user)
    return render(request, 'profile.html', {'title': title, 'following':following, 'follow':follow, 'users':users, 'people_following':people_following})

def single_art(request, art_id): 
    title = 'Creative || Hub'
    arts = Post.objects.get(id=art_id)
    comments = Comments.get_comment_by_image(id = art_id)
    
    current_user = request.user
    if request.method == 'POST':
        form = PostComments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.arts = arts
            comment.user = request.user
            comment.save()
            return redirect('single-art', art_id = art_id )
        
    else:
        form = PostComments()
    return render(request, 'single_art.html', {'arts':arts,'form':form, 'comments':comments, 'title':title})



def follow(request, user_id):
    other_user = User.objects.get(id=user_id)
    follow = Follow.objects.add_follower(request.user, other_user)

    return redirect('single-art')


@login_required(login_url='/accounts/login/')
def unfollow(request, user_id):
    other_user = User.objects.get(id=user_id)

    follow = Follow.objects.remove_follower(request.user, other_user)

    return redirect('single-art')

        
    



