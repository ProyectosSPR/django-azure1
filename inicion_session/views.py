from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import logging
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm








logger = logging.getLogger("login_view")
@login_required
def home_view(request):
    return render(request, "home.html")




def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"Usuario {user.username} ha iniciado sesión")

            return redirect('home')
        else:
            return HttpResponse('Invalid login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("login")



@login_required
def profile_view(request):
    return render(request, "profile.html")
