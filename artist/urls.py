from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.home, name='index'),
    path('postImage/', views.post_image, name='postImage'),
    path('photos', views.photos, name='photos')
]