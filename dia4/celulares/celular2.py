class Celular():
    def __init__(self, tamanio = 0):
        self.tamanio = tamanio

    def __eq__(self, other):
        print(self.tamanio,other.tamanio)
        return self.tamanio == other.tamanio
    
android = Celular(16)
iphone = Celular(16)

print(android)#
print(iphone)#
print(android == iphone)#False