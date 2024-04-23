from usuario import Usuario
from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    """
    Clase que representa una encuesta.
    Atributos:
        nombre (str): Nombre de la encuesta.
        preguntas (list): Lista de preguntas de la encuesta.
        listado_respuestas (list): Lista de listados de respuestas de la encuesta.
    """
    # Paso1: Definir la clase Encuesta.
    def __init__(self, nombre: str):
        # Constructor de la clase Encuesta para iniciar los atributos.
        self.__nombre = nombre  # Nombre de la encuesta.
        self.__preguntas = []   # Lista para almacenar las preguntas de la encuesta.
        self.__listado_respuestas = []  # Lista para almacenar los listados de respuestas de la encuesta.

    def agregar_pregunta(self, pregunta: Pregunta): # Método para agregar una pregunta a la encuesta.
        self.__preguntas.append(pregunta)

    def agregar_respuestas(self, respuestas: ListadoRespuestas): # Método para agregar un listado de respuestas a la encuesta.
        self.__listado_respuestas.append(respuestas)

    def mostrar_encuesta(self):
        print(f"Encuesta: {self.__nombre}") # Método para mostrar la información de la encuesta y sus preguntas.
        for pregunta in self.__preguntas:
            pregunta.mostrar()

    # Propiedad para acceder al nombre de la encuesta
    @property
    def nombre(self) -> str:
        return self.__nombre
    # Setter para modificar el nombre de la encuesta
    @nombre.setter
    def nombre(self, valor: str):
        self.__nombre = valor

class EncuestaLimitadaEdad(Encuesta):
    """
    Clase que representa una encuesta limitada por edad.
    Atributos:
        nombre (str): Nombre de la encuesta.
        edad_minima (int): Edad mínima permitida para participar en la encuesta.
        edad_maxima (int): Edad máxima permitida para participar en la encuesta.
    """
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int):
        super().__init__(nombre)
        # Paso 2: Iniciar los atributos de edad mínima y máxima
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    @property
    def edad_minima(self) -> int:
        return self.__edad_minima

    @edad_minima.setter
    def edad_minima(self, valor: int):
        if isinstance(valor, int): # Validar que el valor de edad mínima sea un número entero.
            self.__edad_minima = valor
        else:
            raise ValueError("La edad mínima debe ser un número entero.")

    @property
    def edad_maxima(self) -> int:
        return self.__edad_maxima

    @edad_maxima.setter
    def edad_maxima(self, valor: int):
        if isinstance(valor, int):# Validar que el valor de edad máxima sea un número entero.
            self.__edad_maxima = valor
        else:
            raise ValueError("La edad máxima debe ser un número entero.")

    def validar_edad(self, usuario: Usuario) -> bool:
        return self.edad_minima <= usuario.edad <= self.edad_maxima # Verificar si la edad del usuario está dentro del rango permitido.

    def agregar_respuesta(self, respuestas: "ListadoRespuestas"):
        if self.validar_edad(respuestas.usuario): # Verificar si el usuario cumple con el rango de edad permitido.
            super().agregar_respuestas(respuestas)
        else:
            print("El usuario no se encuentra dentro del rango de edad requerido para participar en esta encuesta")

class EncuestaLimitadaRegion(Encuesta):
    """
    Clase que representa una encuesta limitada por región.
    Atributos:
        nombre (str): Nombre de la encuesta.
        regiones_permitidas (list): Lista de regiones permitidas para participar en la encuesta.
    """
    def __init__(self, nombre: str, regiones_permitidas: list):
        super().__init__(nombre)
        # Paso 3: Iniciar las regiones permitidas.
        self.regiones_permitidas = regiones_permitidas

    @property
    def regiones_permitidas(self) -> list:
        return self.__regiones_permitidas

    @regiones_permitidas.setter
    def regiones_permitidas(self, valor: list):
        if isinstance(valor, list): # Validar que el valor de las regiones permitidas sea una lista.
            self.__regiones_permitidas = valor
        else:
            raise ValueError("Las regiones permitidas deben ser una lista.")

    def validar_region(self, usuario: Usuario) -> bool: # Verificar si la región del usuario está en la lista de regiones permitidas.
        return usuario.region in self.regiones_permitidas

    def agregar_respuesta(self, respuestas: "ListadoRespuestas"):
        if self.validar_region(respuestas.usuario): # Verificar si el usuario cumple con la región permitida.
            super().agregar_respuestas(respuestas)
        else:
            print("Lo sentimos, el usuario no cumple con este requisito para esta encuesta.")

if __name__ == "__main__":
    print("Bienvenido al sistema de encuestas.")

    # Paso 4: Solicitar al usuario que ingrese su información personal.
    nombre = input("Ingrese su nombre de usuario: ")
    correo = input("Ingrese su correo electrónico: ")

    # Encuesta de Edad.
    print("\nEncuesta de Edad:")
    print("Por favor, seleccione el rango de edad que mejor represente su grupo:\n"
        "1. 20-29 años\n"
        "2. 30-39 años\n"
        "3. 40-49 años\n"
        "4. 50-59 años\n"
        "5. 60 o más años\n")
    while True:
        opcion_edad = input("Ingrese el número que corresponde a su grupo de edad: ")
        if opcion_edad in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("El usuario no se encuentra dentro del rango de edad requerido para participar en esta encuesta")

    # Convertir la opción de edad a un rango de edad.
    if opcion_edad == "1":
        edad = (20, 29)
    elif opcion_edad == "2":
        edad = (30, 39)
    elif opcion_edad == "3":
        edad = (40, 49)
    elif opcion_edad == "4":
        edad = (50, 59)
    else:
        edad = (60, 150)  
        
    if not (18 <= edad[0] <= 60): # Validar la edad ingresada.
        print("La edad ingresada no está dentro del rango permitido (18 a 60 años).")
        exit()

    # Encuesta de Región.
    print("\nEncuesta de Región:")
    print("Por favor, seleccione la región en la que vive:\n"
        "1. Arica y Parinacota\n"
        "2. Tarapacá\n"
        "3. Antofagasta\n"
        "4. Atacama\n"
        "5. Coquimbo\n"
        "6. Valparaíso\n"
        "7. Metropolitana de Santiago\n"
        "8. Libertador General Bernardo O'Higgins\n"
        "9. Maule\n"
        "10. Ñuble\n"
        "11. Biobío\n"
        "12. La Araucanía\n"
        "13. Los Ríos\n"
        "14. Los Lagos\n"
        "15. Aysén del General Carlos Ibáñez del Campo\n"
        "16. Magallanes y de la Antártica Chilena\n")
    while True:
        opcion_region = input("Ingrese el número que corresponde a su región: ")
        if opcion_region in [str(i) for i in range(1, 17)]:
            break
        else:
            print("Lo sentimos, el usuario no cumple con este requisito para esta encuesta.")

    regiones = [  # Convertir la opción de región a la región correspondiente.
        "Arica y Parinacota", "Tarapacá", "Antofagasta", "Atacama",
        "Coquimbo", "Valparaíso", "Metropolitana de Santiago",
        "Libertador General Bernardo O'Higgins", "Maule", "Ñuble",
        "Biobío", "La Araucanía", "Los Ríos", "Los Lagos",
        "Aysén del General Carlos Ibáñez del Campo", "Magallanes y de la Antártica Chilena"
    ]
    region = regiones[int(opcion_region) - 1]

    # Crear el usuario con la información ingresada.
    usuario = Usuario(nombre, correo, edad, region)

    # Crear la pregunta de región y la encuesta de región.
    pregunta_region = Pregunta("¿En qué región vives?")
    encuesta_region = EncuestaLimitadaRegion("Encuesta de Región", regiones)

    # Crear un ListadoRespuestas para las respuestas del usuario para la encuesta de región.
    respuestas_region = ListadoRespuestas(usuario)
    respuestas_region.agregar_respuesta(pregunta_region, region)
    encuesta_region.agregar_respuestas(respuestas_region)
    print("¡Gracias por participar en la encuesta!")