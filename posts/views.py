from django.http import HttpResponse

def index(request):
    #body
    return HttpResponse("Hello, world. You're at the posts index.")