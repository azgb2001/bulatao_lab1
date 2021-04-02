from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NameForm



def home(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'home.html',{'Submit': form.cleaned_data['fname']})
        else:
            return render(request, 'home.html', {'form': form})
    else:
        form = NameForm()
    return render(request, 'home.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def key(request):
    return render(request, 'key.html')

def thisweek(request):
    return render(request, 'thisweek.html')

def today(request):
    return render(request, 'today.html')

