# Paso 1: Importar la clase Producto desde el módulo producto.py
from producto import Producto

# Paso 2: Definir la clase base Tienda.
class Tienda:
    # Paso 3: Método constructor para iniciar los atributos de la tienda.
    def __init__(self, nombre, costo_delivery):
        # Paso 4: Encapsulamiento de los atributos de la tienda.
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        # Paso 5: Iniciar una lista vacía para almacenar los productos de la tienda.
        self.__productos = []

    def ingresar_producto(self, producto):# Método para ingresar un producto a la tienda.
        for p in self.__productos: # Verificar si el producto ya existe en la tienda.
            if p.obtener_nombre() == producto.obtener_nombre():
                p.actualizar_stock(producto.obtener_stock())#Si el producto ya existe, actualizar su stock.
                return
        self.__productos.append(producto) # Si el producto no existe, agregarlo a la lista de productos.

    # Paso 6: Método para listar los productos de la tienda.
    def listar_productos(self):
        return self.__productos

    # Paso 7: Método para realizar una venta en la tienda.
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos: # Buscar el producto por su nombre.
            if producto.obtener_nombre() == nombre_producto:

                if producto.obtener_stock() >= cantidad:# Verificar si hay suficiente stock para realizar la venta.
                    producto.actualizar_stock(-cantidad)# Actualizar el stock del producto después de la venta.
                    print("Realizando venta...")
                    return True
                else:
                    print("No hay suficiente stock para realizar la venta.")
                    return False
        print("El producto no está disponible en la tienda.")
        return False

# Paso 8: Definir subclases específicas para cada tipo de tienda.
class Restaurante(Tienda):
    pass  

class Supermercado(Tienda):
    pass  

class Farmacia(Tienda):
    # Paso 9: Sobreescribir el método realizar_venta para aplicar reglas específicas de la farmacia.
    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:# Aplicar regla: no se puede vender más de 3 unidades por venta en la farmacia.
            print("No se puede vender más de 3 unidades por venta en la farmacia.")
            return False
        return super().realizar_venta(nombre_producto, cantidad)#Llamar al método realizar_venta de la clase padre (Tienda) utilizando super()