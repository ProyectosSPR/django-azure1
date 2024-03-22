from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
from django.contrib.auth import logout
import logging

logger = logging.getLogger(__name__)


@login_required
def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "profile.html")


def registrar(request):
    if request.method == "GET":
        return render(request, "registrar.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # REGISTRAR USUARIO
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                username = (request.POST["username"],)
                return redirect("login")  # Redirigir al formulario de inicio de sesión
            except:
                return render(
                    request,
                    "registrar.html",
                    {
                        "form": UserCreationForm,
                        "error": "No se pudo registrar usuario ya existe",
                    },
                )

    return render(
        request,
        "registrar.html",
        {"form": UserCreationForm, "error": "contraseña no coinciden"},
    )


def logout_custom(request):
    logout(request)
    return redirect("login")


def login_view(request):
    errors = None
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            logger.info(
                f"Usuario {user.username} ha iniciado sesión"
            )  # Registra un mensaje informativo
            return redirect("profile")
        else:
            logger.error("Error en el formulario de inicio de sesión: %s", form.errors)
            errors = form.errors
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form, "errors": errors})
