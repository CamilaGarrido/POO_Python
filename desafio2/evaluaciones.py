from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipo_masa# Importar las listas de ingredientes desde el archivo ingredientes.py
from pizza import Pizza

# A. Imprimir los atributos de clase de la clase Pizza.
print("Listado de ingredientes y tipos de masa disponibles:")
print("Ingredientes proteicos:", ingredientes_proteicos)
print("Ingredientes vegetales:", ingredientes_vegetales)
print("Tipos de masa:", tipo_masa)

# B. Verificar si salsa de tomate está presente en la lista. 
if Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]):
    print("El elemento salsa de tomate está presente en la lista.")
else:
    print("El elemento salsa de tomate no está presente en la lista.")

# C. Crear una nueva instancia de la clase Pizza.
pizza_nueva = Pizza()
pizza_nueva.realizar_pedido()

# D. Imprimir detalle del pedido.
print("\nDetalle del pedido:")
if pizza_nueva.es_valida:
    print("Ingrediente proteico:", pizza_nueva.ingrediente_proteico)
    print("Ingredientes vegetales:", pizza_nueva.ingrediente_vegetal_1, "y", pizza_nueva.ingrediente_vegetal_2)
    print("Tipo de masa:", pizza_nueva.tipo_masa)
    print("Tamaño de la pizza:", pizza_nueva.tamaño)
    print("Precio de la pizza:", pizza_nueva.precio)
    print("¿Es un pedido de pizza válido? Sí")
else:
    print("Pedido no válido. Por favor, ingrese valores válidos.")

# E. Mostrar si la clase Pizza es una pizza válida o no.
print("¿Es la clase Pizza una pizza válida?", "Sí" if Pizza.validar_pedido(pizza_nueva) else "No")