# Paso 1: Importar la excepción LargoExcedidoException y la clase datetime desde los módulos correspondientes.
from error import LargoExcedidoException
from datetime import datetime

# Paso 2: Definir la clase Anuncio y sus métodos.
class Anuncio: 
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.ancho = ancho if ancho > 0 else 1  # Validar el ancho.
        self.alto = alto if alto > 0 else 1  # Validar el alto.
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo
    
    def tipo_anuncio(self):
        return "Anuncio"  

# Paso 3: Definir las subclases.
class Video(Anuncio):
    def tipo_anuncio(self): # Definir la subclase Video que hereda de Anuncio.
        return "Video" 

class Display(Anuncio):
    def tipo_anuncio(self): # Definir la subclase Display que hereda de Anuncio.
        return "Display"  

class Social(Anuncio):
    def tipo_anuncio(self): # Definir la subclase Social que hereda de Anuncio.
        return "Social"  

class Campania:
    def __init__(self, nombre: str, fecha_inicio: datetime, fecha_termino: datetime, anuncios: list):
        # Paso 4: Iniciar la clase Campania.
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios  # Lista para almacenar los anuncios.

    def __str__(self):
        # Método sobrecargado para retornar información de la campaña.
        cant_video = 0  # Contadores para cada tipo de anuncio.
        cant_display = 0
        cant_social = 0
        for elemento in self.__anuncios: # Contar la cantidad de cada tipo de anuncio.
            tipo = elemento.tipo_anuncio()
            if tipo == "Video":
                cant_video += 1
            elif tipo == "Display":
                cant_display += 1
            elif tipo == "Social":
                cant_social += 1
        return f"""
        Nombre de la campaña: {self.__nombre}
        Anuncios: 
        Video: {cant_video}, Display: {cant_display}, Social: {cant_social}
        """

    def modificar_nombre(self, nuevo_nombre):  
        # Método para modificar el nombre de la campaña.
        if len(nuevo_nombre) <= 250:
            self.__nombre = nuevo_nombre
        else:
            raise LargoExcedidoException("El nuevo nombre excede los 250 caracteres.")  

    @property  
    def anuncios(self):
        # Getter para el atributo anuncios.
        return self.__anuncios

    @property  
    def fecha_inicio(self):
        # Setter para el atributo fecha_inicio
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, nueva_fecha_inicio):
        self.__fecha_inicio = nueva_fecha_inicio  # Implementar setter para fecha_inicio
    
    @property  
    def fecha_termino(self):
        # Setter para el atributo fecha_termino
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, nueva_fecha_termino):
        self.__fecha_termino = nueva_fecha_termino  # Implementar setter para fecha_termino  

    def anuncios_str(self):
        # Paso 5: Contar la cantidad de cada tipo de anuncio en la campaña.
        tipos_anuncio = {"Video": 0, "Display": 0, "Social": 0}  # Iniciar un diccionario para almacenar la cantidad de cada tipo de anuncio.
        for anuncio in self.__anuncios:
            tipo = anuncio.tipo_anuncio()  # Obtener el tipo de anuncio para cada elemento en la lista de anuncios.
            if tipo in tipos_anuncio:  # Verificar si el tipo de anuncio está en el diccionario.
                tipos_anuncio[tipo] += 1  # Incrementar el contador para ese tipo de anuncio.
        return ", ".join([f"{tipo}: {cantidad}" for tipo, cantidad in tipos_anuncio.items()])  