from django.urls import path

from .views_API import PostListApi, CreatePostApi, PostDetailApi

urlpatterns = [
    path('posts', PostListApi.as_view()),
    path('create/post/', CreatePostApi.as_view()),
    path('post/<int:pk>/', PostDetailApi.as_view()),

]