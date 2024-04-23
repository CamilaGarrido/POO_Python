from alternativa import Alternativa  # Importar la clase Alternativa desde el módulo alternativa.
class Pregunta:
    # Paso 1: Definir el método __init__ para iniciar los atributos de la pregunta.
    def __init__(self, enunciado: str, requerido: bool = True, ayuda: str = None):
        self.__enunciado = enunciado  # Enunciado de la pregunta.
        self.__ayuda = ayuda  # Ayuda opcional para la pregunta.
        self.__es_requerida = requerido  # Indicador de si la pregunta es requerida.
        self.__alternativas = []  # Lista para almacenar las alternativas de la pregunta.

    # Paso 2: Definir propiedades para acceder y modificar los atributos de la pregunta.
    @property
    def enunciado(self) -> str:
        return self.__enunciado #Obtener el enunciado de la pregunta.

    @enunciado.setter
    def enunciado(self, valor: str):
        self.__enunciado = valor # Establecer el enunciado de la pregunta.

    @property
    def ayuda(self) -> str:
        return self.__ayuda #Obtener la ayuda asociada a la pregunta.

    @ayuda.setter
    def ayuda(self, valor: str):
        self.__ayuda = valor  #Establecer la ayuda asociada a la pregunta.

    @property
    def es_requerida(self) -> bool: #Obtener el indicador de si la pregunta es requerida.
        return self.__es_requerida

    @es_requerida.setter
    def es_requerida(self, valor: bool): #Establecer el indicador de si la pregunta es requerida.
        self.__es_requerida = valor

    @property
    def alternativas(self) -> list: # Obtener la lista de alternativas de la pregunta.
        return self.__alternativas

    # Paso 3: Método para agregar una alternativa a la pregunta.
    def agregar_alternativa(self, alternativa: Alternativa):
        self.__alternativas.append(alternativa)

    # Paso 4: Método para mostrar la pregunta.
    def mostrar_pregunta(self):
        resultado = f"Pregunta: {self.__enunciado}"  # Enunciado de la pregunta.
        resultado += f" (Ayuda: {self.__ayuda})" if self.__ayuda else ""  # Agregar ayuda si existe.
        resultado += "\nAlternativas:\n"
        resultado += "\n".join(f" - {alt.mostrar_alternativa()}" for alt in self.__alternativas)
        print(resultado)  # Imprimir la información de la pregunta.