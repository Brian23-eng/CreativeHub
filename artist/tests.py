from django.test import TestCase
from .models import Profile, Post, Comments
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User( username = 'Brian', email = 'g@gmail.com', password = 'beta')
        self.user.save()
        self.profile = Profile( name='Brian', profile_picture = 'test.jpeg',bio='this is a test bio', contact = 0, user=self.user, )
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.prfile, Profile))
        
    def save_profile(self):
        self.profile.save()
        
    def delete_profile(self):
        self.profile.delete()
        
        
class TestPost(TestCase):
    def setUp(self):
        self.user = User( username = 'Brian', email = 'g@gmail.com', password = 'beta')
        self.post = Post( title = 'test post', ig_url = 'https://url.com',description = 'this is a test image', photo = 'https://img.com/345',  user = self.user, date=12/3/2019 )
        
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))
        
    def save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)
        
    def get_post(self):
        self.post.save()
        posts = Post.all_posts() 
        self.assertTrue(len(posts)>0)
        
    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        
class TestComments(TestCase):
        def setUp(self):
            self.user = User( username = 'Brian', email = 'g@gmail.com', password = 'beta')
            self.post = Post( title = 'test post', ig_url = 'https://url.com',description = 'this is a test image', photo = 'https://img.com/345',  user = self.user, date=12/3/2019 )
            self.comment = Comments(comment = 'the best', posted=12/3/2019, image = 'g.jpg')
            
        def test_save_comment(self):
            self.comment.save_post()
            comments = Comments.objects.all()
            self.assertTrue(len(comments)>0)
            
            
        def get_comment(self):
            self.save()
            comment = Comments.all_comments() 
            self.assertTrue(len(comment)>0)
            
            
        def test_delete_comments(self):
            self.comment.delete_comment()
            comment = Comments.objects.all().delete()
            
            
