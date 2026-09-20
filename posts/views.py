from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Comment
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    #body
    return HttpResponse("khgjgj")

#--------------------------post_list
def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/post_list.html', context)

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
#----------------------------

#----------------------------post_deatal
def post_deteal(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except:
        return HttpResponseNotFound('not found')
    comments = Comment.objects.filter(post = post_id)
    context = { 'post' : post, 'comments' : comments}
    return render(request, 'posts/post_deteal.html', context)

'''class PostDteal(generic.DetailView):
    model = Post
    template_name = 'posts/post_deteal.html'

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super(PostDteal, self).get_context_data()
        
        context['comments'] = Comment.objects.filter(post = kwargs['object'].pk)
        return context'''


class PostDeatale(generic.DetailView):
    model = Post
    template_name = 'posts/post_deteal.html'

    def get_context_data(self, **kwargs):
        context = super(PostDeatale, self).get_context_data()
        context['comments'] = Comment.objects.filter(post = kwargs['object'].pk)
        return context
#------------------------------
    
def post_create(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid(): 
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = Post_form()
        return render(request, 'posts/post_create.html', { 'form' : form })


class PostCreateView(generic.CreateView):
    model=Post
    template_name = 'posts/post_create.html'
    fields="__all__"
    context_object_name = 'form'
    success_url = reverse_lazy("post_list")







