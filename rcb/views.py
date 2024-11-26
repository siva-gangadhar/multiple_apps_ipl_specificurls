# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse("King kohli is the captain of the rcb")
def vicecaptain(request):
    return HttpResponse("rajat patidar is the vicecaptain of rcb")






