from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def home(request):
    return render(request, "home.html")


@csrf_protect
def singup(request):
    if request.method == "GET":
        return render(request, "singup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # REGISTRAR USUARIO
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                return HttpResponse("usuario registrado correctamente")
            except:
                return render(
                    request,
                    "singup.html",
                    {
                        "form": UserCreationForm,
                        "error": "No se pudo registrar usuario ya existe",
                    },
                )

    return render(
        request,
        "singup.html",
        {"form": UserCreationForm, "error": "contraseña no coinciden"},
    )
