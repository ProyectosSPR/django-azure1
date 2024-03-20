from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth import login
import logging
=======

from django.contrib.auth import login
import logging

>>>>>>> 8c2a28e0893dbbcfa5747c132c80f882f28f3070

logger = logging.getLogger("login_view")
@login_required
def home_view(request):
    return render(request, "home.html")


import logging
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Crear un logger con el nombre "login_view"
logger = logging.getLogger("login_view")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"Usuario {user.username} ha iniciado sesión")
<<<<<<< HEAD
            return redirect('home')
        else:
            return HttpResponse('Invalid login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    logger.info("cerrado sesion")
    return redirect('login')
=======
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")

>>>>>>> 8c2a28e0893dbbcfa5747c132c80f882f28f3070

@login_required
def profile_view(request):
    return render(request, "profile.html")
