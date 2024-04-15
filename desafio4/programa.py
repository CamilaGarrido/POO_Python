# Paso 1: Importar las clases Restaurante, Supermercado y Farmacia desde el módulo tienda.py.
from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto #importar la clase Producto desde el módulo producto.py.

# Paso 2: Definir una función para mostrar las opciones de tipo de tienda.
def mostrar_opciones_tienda():
    opciones = {
        "1": "Restaurante",
        "2": "Supermercado",
        "3": "Farmacia"
    }
    print("¡Bienvenido!")
    print("Por favor, elige el tipo de tienda:")
    for key, value in opciones.items():
        print(f"{key}. {value}")

# Paso 3: Definir una función para ingresar el tipo de tienda.
def ingresar_tipo_tienda():
    while True:
        tipo_tienda = input("Ingresa el número correspondiente a tu elección: ")
        if tipo_tienda in ["1", "2", "3"]:
            return tipo_tienda
        else:
            print("Por favor, ingresa un número válido.")

# Paso 4: Definir una función para ingresar los datos de la tienda.
def ingresar_datos_tienda():
    nombre_tienda = input("Ingresa el nombre de la tienda: ")
    while True:
        costo_delivery = input("Ingresa el costo de delivery: ")
        if costo_delivery.isnumeric():  # Verificar si la entrada es un número.
            return nombre_tienda, float(costo_delivery)
        else:
            print("Por favor, ingresa un número válido para el costo de delivery.")

# Paso 5: Definir una función para ingresar productos a la tienda.
def ingresar_producto():
    print("\nINGRESO DE PRODUCTOS")
    productos = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto (o enter para terminar): ")
        if not nombre_producto:
            break
        while True:
            precio_producto = input("Ingrese el precio del producto: ")
            try:
                precio_producto = float(precio_producto)
                break  # Salir del bucle si la conversión se completó correctamente.
            except ValueError:
                print("Por favor, ingresa un número válido para el precio del producto.")
        while True:
            stock_producto = input("Ingrese el stock del producto: ")
            if stock_producto.isnumeric():  # Verificar si la entrada es un número.
                stock_producto = int(stock_producto)
                break  # Salir del bucle si la conversión se completó correctamente.
            else:
                print("Por favor, ingresa un número válido para el stock del producto.")
        producto = Producto(nombre_producto, precio_producto, stock_producto)
        productos.append(producto)
        print("Producto ingresado exitosamente.")
    return productos

# Paso 6: Definir una función para mostrar el menú de opciones de la tienda.
def mostrar_menu_opciones(tienda):
    print("\nSelecciona una opción:")
    print("1. Ingresar nuevos productos")
    print("2. Mostrar productos existentes")
    print("3. Realizar venta")
    print("4. Salir")

# Paso 7: Definir la función principal del programa.
def main():
    mostrar_opciones_tienda()
    tipo_tienda = ingresar_tipo_tienda()

    tiendas = {
        "1": Restaurante,
        "2": Supermercado,
        "3": Farmacia
    }
    tienda_seleccionada = tiendas.get(tipo_tienda)
    nombre_tienda, costo_delivery = ingresar_datos_tienda()
    tienda = tienda_seleccionada(nombre_tienda, costo_delivery)

    while True:
        mostrar_menu_opciones(tienda)
        opcion = input("Ingresa el número correspondiente a tu elección: ")

        if opcion == '1':
            productos = ingresar_producto()
            for producto in productos:
                tienda.ingresar_producto(producto)
            print("Productos ingresados exitosamente.")
        elif opcion == '2':
            print("\nProductos existentes en la tienda:")
            productos = tienda.listar_productos()
            for producto in productos:
                print(f"Nombre: {producto.obtener_nombre()}, Precio: {producto.obtener_precio()}, Stock: {producto.obtener_stock()}")
        elif opcion == '3':
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            while True:
                cantidad = input("Ingrese la cantidad a vender: ")
                try:
                    cantidad = int(cantidad)
                    break  # Salir del bucle si la conversión se completó correctamente.
                except ValueError:
                    print("Por favor, ingresa un número válido para la cantidad.")
            venta_exitosa = tienda.realizar_venta(nombre_producto, cantidad)
            if venta_exitosa:
                print("Venta realizada exitosamente.")
            else:
                print("No se pudo realizar la venta.")
        elif opcion == '4':
            print("¡Hasta luego!")
            return
        else:
            print("Por favor, ingresa un número válido.")
if __name__ == "__main__":#Ejecutar la función principal si el archivo se abre directamente.
    main()