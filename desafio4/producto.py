# Paso 1: Definir la clase Producto.
class Producto:
    # Paso 2: Método constructor para iniciar los atributos del producto.
    def __init__(self, nombre, precio, stock=0):
        # Paso 3: Encapsulamiento de los atributos utilizando doble guión bajo (__)
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)#Evitar que el stock llegue a números negativos.

    # Paso 4: Métodos para obtener los atributos del producto.
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock

    # Paso 5: Método para actualizar el stock del producto.
    def actualizar_stock(self, cantidad):
        self.__stock = max(0, self.__stock + cantidad) # Evitar que el stock llegue a números negativos.