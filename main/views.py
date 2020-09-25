from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')
