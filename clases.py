import os


class AgregarRutas:
    def __init__(self, carpetas_a_omitir, directorio_actual=None):
        self.carpetas_a_omitir = carpetas_a_omitir
        self.directorio_actual = directorio_actual or os.getcwd()

    def __str__(self):
        # Obtener la lista de todos los elementos en el directorio
        elementos = os.listdir(self.directorio_actual)

        # Filtrar solo los elementos que son directorios y no están en la lista de carpetas a omitir
        carpetas = [
            elemento
            for elemento in elementos
            if os.path.isdir(os.path.join(self.directorio_actual, elemento))
            and elemento not in self.carpetas_a_omitir
        ]

        # Crear los patrones de URL por cada carpeta restante
        urls = [f"path('', include('{carpeta}.urls'))" for carpeta in carpetas]
        print(carpetas)
        return "\n".join(urls)


rutas = AgregarRutas("static")
print(rutas)
