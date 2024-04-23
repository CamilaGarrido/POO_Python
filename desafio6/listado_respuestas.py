from usuario import Usuario
# Paso 1: Definir la clase ListadoRespuestas.
class ListadoRespuestas:
    def __init__(self, usuario: "Usuario"): # Definir el método __init__ para iniciar los atributos del listado de respuestas.
        self.__usuario = usuario # Usuario asociado al listado de respuestas.
        self.__lista_respuestas = [] # Lista de respuestas del usuario.

    # Paso 2: Método para agregar una respuesta al listado de respuestas.
    def agregar_respuesta(self, pregunta, respuesta):
        self.__lista_respuestas.append((pregunta, respuesta))# Agregar la respuesta a la lista de respuestas.

    # Paso 3: Propiedad para acceder al usuario asociado.
    @property
    def usuario(self) -> "Usuario":
        return self.__usuario

    # Paso 4: Propiedad para acceder a la lista de respuestas.
    @property
    def lista_respuestas(self) -> list:
        return self.__lista_respuestas