from django.shortcuts import render
from http import HttpResponse

def index(request):
    return HttpResponse('Hello,we gonna make dns restapi')