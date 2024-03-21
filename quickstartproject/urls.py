"""quickstartproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from clases import AgregarRutas
from django.contrib.auth.views import LoginView


# Definir las rutas estáticas (por ejemplo, la de administración de Django)
urlpatterns = [
    path("admin/", admin.site.urls),
]

# Crear una instancia de AgregarRutas
agregar_rutas = AgregarRutas(
    [
        ".git",
        ".github",
        ".venv",
        "MyApp",
        "__pycache__",
        "static",
        "quickstartproject",
        "antenv",
        "static",
        "staticfiles",
        "venv",
    ]
)

# Obtener la ruta generada como una cadena de texto
ruta_generada = str(agregar_rutas)

# Dividir la ruta generada en líneas individuales
rutas_generadas = ruta_generada.strip().split("\n")

# Agregar cada ruta generada a urlpatterns
for ruta in rutas_generadas:
    urlpatterns.append(eval(ruta))
