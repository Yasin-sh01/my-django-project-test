from django.http import HttpResponse

# Create your views here.

def profile(request):
    return HttpResponse('it is profile.')
    