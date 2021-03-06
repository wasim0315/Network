from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("submit",views.create,name="create"),
    path("profile/<str:username>",views.viewProfile,name="viewprofile"),
    path("profile/<str:username>/follow",views.follow,name="follow"),
    path("profile/<str:username>/unfollow",views.unfollow,name="unfollow"),
    path("followings",views.viewFollowings,name="followings"),
    path("edit/<int:post_id>",views.edit,name="edit"),
    url(r'^likepost/$', views.like_post, name='like-post'),
]
