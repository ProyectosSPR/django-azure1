from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import logging
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden, HttpResponse








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
            # Log si CSRF token no se envía correctamente
            logger.error("El token CSRF no se envió correctamente en la solicitud.")
            return HttpResponse('Invalid login')
    
    return render(request, 'login.html', {'form': AuthenticationForm()})


def handler403(request, exception):
    # Log el motivo de la denegación
    logger.error(f"Se denegó la solicitud: {exception}")
    return HttpResponseForbidden('403 Forbidden')

def logout_view(request):
    logout(request)
    logger.info("usuario cerro sesion")
    return redirect("login")



@login_required
def profile_view(request):
    return render(request, "profile.html")
