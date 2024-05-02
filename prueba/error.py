# Paso 1: Clase Error para las excepciones.
class Error(Exception):
    pass

# Paso 2: Excepción cuando se intenta asignar un nombre que excede los 250 caracteres.
class LargoExcedidoException(Exception):
    def __init__(self, mensaje="El nuevo nombre excede los 250 caracteres."):
        super().__init__(mensaje)
        
# Paso 3: Excepción cuando se intenta asignar un subtipo inválido a un anuncio.
class SubTipoInvalidoException(Exception):
    def __init__(self, mensaje="El nuevo subtipo no es válido para este tipo de anuncio."):
        super().__init__(mensaje)