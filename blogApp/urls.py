from django.urls import path
from . import views
urlpatterns = [
  path("",views.homePage,name="home-page"),
  path("posts/",views.posts,name="posts-page"),
  path("posts/<slug>",views.post_detials,name="posts-details-page")#/posts/my_firstpost/  
]
