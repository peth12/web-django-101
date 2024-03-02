from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello world peth")

def about(request):
    return HttpResponse("<h1>about me</h1>")

def form(request):
    return HttpResponse("<h1>form save data</h1>")