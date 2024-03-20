from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
import logging

logger = logging.getLogger("login_view")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(f"Usuario {user.username} ha iniciado sesión")
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def inicio(request):
    return render(request, "inicio.html", {"user": request.user})


@login_required
def prueba(request):
    return render(request, "pruebas.html", {"user": request.user})


def cerrar_sesion(request):
    logout(request)
    return redirect("login")
