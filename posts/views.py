from .models import Post, Comment
from django.views import generic
from django.urls import reverse_lazy

class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context['comments'] = Comment.objects.filter(post = kwargs['object'].pk)
        return context

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = "__all__"
    context_object_name = 'form'
    success_url = reverse_lazy("post_list")