from pelota import Pelota

#instancia de clase o creacion del objeto
pelota_futbol = Pelota("Amarillo","Cuero",20)
print(pelota_futbol.color,pelota_futbol.material,pelota_futbol.tamanio)#blanco
print(pelota_futbol.forma)

#instancia de clase, con valor por defecto
pelota_backet = Pelota("Anaranjado", "Caucho")
#atributo de clase
print(pelota_backet.forma)#"redondeada"
print(pelota_backet.tamanio)#0
print(pelota_backet.color)#"Anaranjado"
pelota_backet.tamanio= 15
print(pelota_backet.tamanio)

#atributo de clase
print(Pelota.forma)

print(pelota_futbol.color_y_material)
#accesador del atributo (get)
print("con property",pelota_futbol.colores)
print("metodo get",pelota_futbol.getColor())

#mutadores 
#por default
pelota_futbol.color = "Negro"
print("por default",pelota_futbol.color)
#a traves de metodo
pelota_futbol.setColor("Roja")
print("con metodo",pelota_futbol.color)
#a traves de setter
pelota_futbol.colores = ""
print("con setter",pelota_futbol.color)


