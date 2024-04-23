class Alternativa:
    def __init__(self, contenido: str, ayuda: str = None):
        # Paso 1: Constructor de la clase Alternativa. Se inicia los atributos contenido y ayuda.
        self.contenido = contenido  # Contenido de la alternativa (texto).
        self.ayuda = ayuda  # Ayuda asociada a la alternativa (texto opcional).

# Paso 2: Método para mostrar la alternativa.
    def mostrar_alternativa(self) -> str:
        return f"{self.contenido} (Ayuda: {self.ayuda})" if self.ayuda else self.contenido  # Si hay ayuda disponible, se muestra junto con el contenido.
        # De lo contrario, solo se muestra el contenido.