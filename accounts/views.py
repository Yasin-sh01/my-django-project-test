from django.shortcuts import render
from django.http import HttpResponse

def accounts(request):
    return HttpResponse("this is accounts page")