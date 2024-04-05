#Paso 1: Crear clase y atributos de clase para los precios de los diferentes formatos de té.
class Te:
    duracion = 365 # Tiempo de duración para los té 1 año o 365 días.
    precio_formato_300gr = 3000
    precio_formato_500gr = 5000

#Paso 2:Agregar un método estático que retorne el tiempo de preparación y la recomendación correspondiente.
    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        if sabor == 1:  # Té negro.
            tiempo = 3 # 3 minutos.
            recomendacion = "Se recomienda consumir al desayuno."
        elif sabor == 2:  # Té verde.
            tiempo = 5 # 5 minutos.
            recomendacion = "Se recomienda consumir al medio día."
        elif sabor == 3:  # Agua de hierbas.
            tiempo = 6 # 6 minutos.
            recomendacion = "Se recomienda consumir al atardecer."
        else:
            tiempo = None
            recomendacion = None
        return tiempo, recomendacion
#Paso 3: Agregar un método estático que retorne el precio según el formato ingresado por parámetro (número entero).
    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            precio = Te.precio_formato_300gr
        elif formato == 500:
            precio = Te.precio_formato_500gr
        else:
            precio = None
        return precio