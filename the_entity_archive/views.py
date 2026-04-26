from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def archive(request):
    return HttpResponse("Welcome to the Entity Archive!")
