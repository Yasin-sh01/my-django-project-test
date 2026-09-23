from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name = 'post_list'),
    path('<int:pk>/', PostDetailView.as_view()),
    path('create/', PostCreateView.as_view())
    
    
]
