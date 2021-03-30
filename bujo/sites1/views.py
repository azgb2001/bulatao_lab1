from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import IndexCardForm



def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def key(request):
    return render(request, 'key.html')

def thisweek(request):
    return render(request, 'thisweek.html')

def today(request):
    return render(request, 'today.html')

