"""
URL configuration for my_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import index
from profiles.views import profile
from accounts.views import accounts
from posts.views import post_list, post_deteal, post_create, PostList, PostDeatale, PostCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('profile/', profile),
    path('accounts/', accounts),
    #path('posts/', post_list),
    path('posts/', PostList.as_view(), name='post_list'),
    #path('posts/create/', post_create),
    #path('posts/<int:post_id>/', post_deteal),
    path('posts/<int:pk>/', PostDeatale.as_view()),
    path('posts/create/', PostCreateView.as_view())
    
    
]
