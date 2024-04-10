class Celular():
    def __init__(self, tamanio = 0):
        self.tamanio = tamanio 

android = Celular(16)
iphone = Celular(16)

print(android)#<__main__.Celular object at 0x103eaa120>
print(iphone)#<__main__.Celular object at 0x103eaa210>
print(android == iphone)#False

windowp = android
print(windowp)#<__main__.Celular object at 0x103eaa120>