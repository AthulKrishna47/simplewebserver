from django.shortcuts import render
from django.http import HttpResponrenderse

def home(request):
    return render(request, 'home.html')

# Create your views here.
