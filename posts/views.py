from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Post, Comment
from .forms import Post_form

def index(request):
    #body
    return HttpResponse("khgjgj")

def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'posts/post_list.html', context)


def post_deteal(request, post_id):
    try:
        post = Post.objects.get(pk = post_id)
    except:
        return HttpResponseNotFound('not found')
    comments = Comment.objects.filter(post = post_id)
    context = { 'post' : post, 'comments' : comments}
    return render(request, 'posts/post_deteal.html', context)


def post_create(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid(): 
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = Post_form()
        return render(request, 'posts/post_create.html', { 'form' : form })












'''def post_create(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = Post_form()
    return render(request, 'posts/post_create.html', {'form' : form})'''