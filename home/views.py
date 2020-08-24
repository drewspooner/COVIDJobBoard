from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'home/index.html')

def search(request):
    return render(request, 'home/search.html')

def status(request):
    return render(request, 'home/status.html')

def about(request):
    return render(request, 'home/about.html')