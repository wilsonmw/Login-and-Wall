from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


# Create your views here.
def index(request):
    return render(request, 'loginandwall_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    for error in results['errors']:
        messages.error(request, error)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status']==False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        for error in results['errors']:
            messages.error(request, error)
        return render(request, 'loginandwall_app/success.html')


