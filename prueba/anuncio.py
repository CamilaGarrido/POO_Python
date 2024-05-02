from error import SubTipoInvalidoException  # Importar la excepción personalizada SubTipoInvalidoException.
from abc import ABC, abstractmethod  # Importar la clase ABC para definir clases abstractas.

class Anuncio(ABC):    
    # Paso 1: Definir la clase anuncio y sus métodos.
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str): # Constructor de la clase Anuncio.
        # Iniciar los atributos.
        self.__ancho = ancho if ancho > 0 else 1  # validación del ancho.
        self.__alto = alto if alto > 0 else 1  # validación del alto.
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    # Métodos abstractos que se implementan en las subclases.
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @abstractmethod
    def modificar_subtipo(self, nuevo_subtipo):
        pass

    # Método estático para mostrar formatos y subtipos disponibles para crear anuncios.
    @staticmethod
    def mostrar_formatos():
        print("Tipos de formatos para hacer anuncios:")
        for cls in Anuncio.__subclasses__(): # Iterar sobre las subclases de anuncio para obtener los formatos y subtipos.
            print(f"{cls.FORMATO}:")
            print("=" * len(cls.FORMATO))
            for subtipo in cls.SUBTIPOS:
                print("-", subtipo)
            print()

    # Getters para obtener valores de atributos.
    @property # Método getter para ancho.
    def ancho(self):
        return self.__ancho

    @property # Método getter para alto.
    def alto(self):
        return self.__alto

    @property # Método getter para url_archivo.
    def url_archivo(self):
        return self.__url_archivo

    @property # Método getter para url_clic.
    def url_clic(self):
        return self.__url_clic

    @property # Método getter para sub_tipo.
    def sub_tipo(self):
        return self.__sub_tipo

    # Setters para modificar valores de atributos.
    @ancho.setter # Método setter para ancho.
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1  # Validar para asegurar que el valor sea positivo.

    @alto.setter # Método setter para alto
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1 # Validar para asegurar que el valor sea positivo.

    @url_archivo.setter #Método setter para url_archivo.
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @url_clic.setter  #Método setter para url_clic.
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    @sub_tipo.setter # Método setter para sub_tipo.
    def sub_tipo(self, sub_tipo):
        self.__sub_tipo = sub_tipo

# Paso 2: Definir las subclases Video, Display y Social.
class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):# Constructor de Video
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)  # Llamar al constructor de la clase padre.
        self.__duracion = duracion if duracion > 0 else 5  # Duración del video.

    def modificar_subtipo(self, nuevo_subtipo): # Método para modificar el subtipo del anuncio de video.
        if nuevo_subtipo not in self.SUBTIPOS:
            raise SubTipoInvalidoException("El nuevo subtipo no es válido para este tipo de anuncio.")
        self.sub_tipo = nuevo_subtipo  #validar subtipo.

    def comprimir_anuncio(self):  # Método para comprimir el anuncio de video. 
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self): # Método para redimensionar el anuncio de video. 
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    def tipo_anuncio(self):  # Método para obtener el tipo de anuncio
        return self.FORMATO

class Display(Anuncio):# Subclase Display que hereda de Anuncio.
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")

    def comprimir_anuncio(self): # Método para comprimir el anuncio de display 
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self): # Método para redimensionar el anuncio de display 
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):# Subclase Social que hereda de Anuncio.
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self): # Método para comprimir el anuncio de redes sociales 
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self): # Método para redimensionar el anuncio de redes sociales 
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")