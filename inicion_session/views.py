from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib.auth import login
import logging

logger = logging.getLogger("login_view")
=======
from django.http import HttpResponse
from django.template.context_processors import csrf
>>>>>>> 3fd1a0829ccafd5c619a45a7c9c978541283bf89

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
<<<<<<< HEAD
            logger.info(f"Usuario {user.username} ha iniciado sesión")
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
=======
            return redirect('home')
        else:
            return HttpResponse('Invalid login')
    context = {}
    context.update(csrf(request))
    
    return render(request, 'login.html', context)
>>>>>>> 3fd1a0829ccafd5c619a45a7c9c978541283bf89

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'profile.html')
