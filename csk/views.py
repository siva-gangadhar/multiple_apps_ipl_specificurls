from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse("Rutu is the captain of the csk")
def vicecaptain(request):
    return HttpResponse("jadeja is the vicecaptain of rcb")






