from django.shortcuts import render 
from django.http import HttpResponseRedirect 
from django.urls import reverse
from django.contrib.auth import authenticate , logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    if request.method == "GET":
        return render(request, 'app/index.html')

def login_view(request):
    if request.method == "GET":
        return render(request , 'app/login.html')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'app/login.html',{
                "mensaje": "usuario y/o contraseña incorrecto"
            })

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))