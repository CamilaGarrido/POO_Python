class Usuario:# Definir la clase Usuario
    def __init__(self, nombre: str, correo: str, edad: int, region: int):
        # Paso 1: Iniciar los atributos del usuario.
        self.nombre = nombre  # Nombre del usuario
        self.correo = correo  # Correo electrónico del usuario
        self.edad = edad  # Edad del usuario
        self.region = region  # Región del usuario

    def contestar_encuesta(self, encuesta) -> None: # Método para contestar una encuesta.
        print(f"Contestando la encuesta: {encuesta.nombre}")

    # Propiedad y setter para el nombre del usuario.
    @property  
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    # Propiedad y setter para el correo del usuario.
    @property
    def correo(self) -> str:
        return self.__correo
    @correo.setter
    def correo(self, nuevo_correo: str) -> None:
        self.__correo = nuevo_correo

    # Propiedad y setter para la edad del usuario.
    @property
    def edad(self) -> int:
        return self.__edad
    @edad.setter
    def edad(self, nueva_edad: int) -> None:
        self.__edad = nueva_edad

    # Propiedad y setter para la región del usuario.
    @property
    def region(self) -> int:
        return self.__region
    @region.setter
    def region(self, nueva_region: int) -> None:
        self.__region = nueva_region