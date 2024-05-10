from django.shortcuts import render,get_object_or_404
from . models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .form import RegisterForm


# Create your views here.
def home(request):
    car = Car.objects.all()
    context = {"car":car}
    return render(request,"car/home.html",context)

def book(request):
    context = {}
    return render(request,"car/book.html",context)

def details(request):
    car = Car.objects.all()
    context = {"car":car}
    return render(request,"car/Details.html",context)

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'car/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'car/register.html', {'form': form})

    

def Logout(request):
    Logout(request,User)
    return render(request,"car/home.html",context)

def receipt(request):
    context = {}
    return render(request,"car/receipt.html",context)
