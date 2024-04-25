from error import DimensionError  # Importar clase DimensionError desde el módulo error.

# Paso 1: Definir la clase Foto.
class Foto():
    MAX = 2500  # Máximo permitido para ancho y alto.
    def __init__(self, ancho: int, alto: int, ruta: str) -> None: # Constructor de la clase
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta  

    @property # Propiedad para obtener el ancho.
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter  # Setter para el ancho
    def ancho(self, ancho) -> None:
        try:
            if ancho < 1 or ancho > self.MAX:
                raise DimensionError("El valor de ancho es inválido", ancho, self.MAX)  # Requisito: Lanzar DimensionError si está fuera de rango.
            self.__ancho = ancho
        except DimensionError as e:  
            print(e)  # Imprimir el mensaje de error.

    @property  # Propiedad para obtener el alto
    def alto(self) -> int:
        return self.__alto

    @alto.setter  # Setter para el alto
    def alto(self, alto) -> None:
        try:
            if alto < 1 or alto > self.MAX:
                raise DimensionError("El valor de alto es invalido", alto, self.MAX)  # Requisito: Lanzar un DimensionError si está fuera de rango.
            self.__alto = alto
        except DimensionError as e: 
            print(e)  # Imprimir el mensaje de error.

# Paso 2: Código principal.
try:
    print("¡Bienvenido a la Galería de Fotografías!\nSiga las instrucciones para ingresar las dimensiones (ancho x alto) de su fotografía\n")
    foto_valida = Foto(1000, 2500, "https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg")
    foto_valida.ancho = int(input("Por favor, indique el ancho de su fotografía: "))
    foto_valida.alto = int(input("Por favor, indique el alto de su fotografía: "))
    print(f"Las dimensiones de su fotografía son: {foto_valida.ancho} X {foto_valida.alto}")
except (DimensionError, ValueError):
    print("Error: Las dimensiones ingresadas no son válidas.")