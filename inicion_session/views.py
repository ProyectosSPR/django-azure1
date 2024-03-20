from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth import login
import logging

logger = logging.getLogger("login_view")
@login_required
def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info(f"Usuario {user.username} ha iniciado sesión")
            return redirect('home')
        else:
            return HttpResponse('Invalid login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    logger.info("cerrado sesion")
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'profile.html')
