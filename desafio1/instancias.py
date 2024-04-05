from te import Te #Importar la clase Te del archivo te.py

# Paso 1: Crear dos instancias.
te1 = Te()
te2 = Te()

# Paso 2: Almacenar el tipo de dato de cada instancia en una variable.
tipo_te1 = type(te1)
tipo_te2 = type(te2)

# Paso 3: Mostrar el valor de cada tipo de dato almacenado.
print("Tipo de dato de la instancia te1:", tipo_te1)
print("Tipo de dato de la instancia te2:", tipo_te2)

# Paso 4: Comparar ambos tipos.
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo.")# mostrar resultado.
else:
    print("Los objetos no son del mismo tipo.")# mostrar resultado.