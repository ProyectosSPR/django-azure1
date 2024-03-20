from django.urls import path
from . import views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("inicio/", views.inicio, name="inicio"),  # Agrega esta línea
    path("cerrar-sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("prueba/", views.prueba, name="prueba"),
    # Otras rutas de tu aplicación
]
