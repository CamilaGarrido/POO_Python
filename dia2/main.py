# cambiar el estado es cambiar el valor del atributo
#metodo se asocia a una funcion creada dentro de una clase.
#clases es una caracterisitica generica

from pelota import Pelota

class Usuario():
    nombre = "Julio"

julio = Usuario()
print(julio.nombre)

camilo = Usuario()
print(camilo.nombre)
camilo.nombre = "Camilo"
print(camilo.nombre)
print(julio.nombre)
print("")

pelota_multicolor = Pelota()

#print(pelota_multicolor.color)#AttributeError: 'Pelota' object has no attribute 'color'

#inicializar un atributo de instancia con valor inicial
pelota_multicolor.inicia_color()

# Se asigna color a la instancia
pelota_multicolor.asigna_color("rojo")
print(pelota_multicolor.color)#

# Se lee color. La salida será "El color de esta pelota es rojo"
pelota_multicolor.lee_color()
pelota_multicolor.asigna_color("verde")

# Las salidas serán:
# El color de esta pelota es verde
# El color amarillo NO es el color de ESTA pelota
pelota_multicolor.lee_color_local_y_atributo("amarillo")