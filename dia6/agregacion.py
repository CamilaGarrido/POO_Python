class Material():
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota():
    def __init__(self, tamanio: int, color: str, material: Material):
        self.tamanio = tamanio
        self.color = color
        # La pelota tiene un material
        #al atributo de instancia, se le asigna el objeto
        self.material = material #agregacion
        #self.material = Material(nombre="Metal",duracion="Años",textura = "Aspera")#composicion


# El material existe en forma independiente de la pelota
objeto_material = Material("Plástico", "Corta", "Lisa")
objeto_pelota = Pelota(16, "Amarillo", objeto_material)

print(type(objeto_pelota.material))# Salida: <class '__main__.Material'>
# Salida: Plástico
print(objeto_pelota.material.nombre)
print(objeto_pelota.material.duracion)
print(objeto_pelota.material.textura)

print(objeto_material.duracion)