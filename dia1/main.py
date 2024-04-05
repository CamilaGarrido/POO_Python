from pelota import Pelota

#instancia
pelota_de_andy = Pelota()
print(pelota_de_andy.forma)
print(pelota_de_andy.posiciones)
print(pelota_de_andy.crear_rebote())

#invocacion a metodo estatico 
print(Pelota.crear_rebote())
Pelota.imprimir_posiciones()
print(Pelota.posiciones)
print("")
#llamar a metodo NO estatico
#Pelota.rebotar()#TypeError: Pelota.rebotar() missing 1 required positional argument: 'self'
pelota_de_andy.rebotar()

print(Pelota.posiciones, Pelota.forma)
print(pelota_de_andy.posiciones, pelota_de_andy.forma)

pelota_de_tenis =Pelota()
print(pelota_de_tenis.posiciones, pelota_de_tenis.forma)