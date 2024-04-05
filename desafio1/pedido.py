#Paso 1:Importar la clase Te.
from te import Te  
#Paso 2: Mostrar opciones y solicitudes.
print("¡Bienvenido! Emprendimiento dedicado a la venta de té de hoja artesanal")  # Mensaje de bienvenida.

print("Seleccione el sabor de té:")  # Mostrar las opciones de sabor de té.
print("1 (para té negro)")
print("2 (para té verde)")
print("3 (para agua de hierbas)")

sabor = int(input("Ingrese un número: "))  # Solicitar que se ingrese un numero para escojer el sabor del té.

print("Seleccione el formato del té:")  # Mostrar las opciones de formato de té.
print("300 (para 300 gramos)")
print("500 (para 500 gramos)")
formato = int(input("Ingrese el valor: "))# Solicitar que se ingrese un valor para escojer el formato del té.

# Paso 3: Utilizar métodos de la clase Te para obtener el resto de valores para el pedido.
precio = Te.obtener_precio(formato)  
tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor)

# Paso 4: Mostrar en detalle el pedido.
print("\nDetalle del pedido:") 
print("Sabor del té:", end=' ')
if sabor == 1:
    print("Té negro")
elif sabor == 2:
    print("Té verde")
elif sabor == 3:
    print("Agua de hierbas")
print("Formato del té:", formato, "gramos")
print("Precio del té: $", precio)
print("Tiempo de preparación:", tiempo, "minutos")
print("Recomendación:", recomendacion)
print("¡Gracias por tu pedido! Disfruta de nuestro té artesanal. ¡Vuelve pronto!")# Mensaje de agradecimiento y despedida.