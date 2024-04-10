#se importa para crear una clase abstracta
from abc import ABC, abstractmethod

class Pelota(ABC):
    #definicion del metodo, no tiene implementación
    @abstractmethod
    def rebotar(self, altura: int):
        pass

#TypeError: Can't instantiate abstract class Pelota without an implementation for abstract method 'rebotar'
#pelotita = Pelota()#NO SE PUEDE INSTANCIA UNA CLASE ABSTRACTA

class PelotaDeJuguete(Pelota):
    
    def __init__(self, color: str):
        self.rebotes=[]
        #_ _ para definir atributo privado
        self.__color = color

    #ES OBLIGATORIO implementar el metodo que es abstracto
    def rebotar(self, altura: int):
        print(altura)

    #metodo get -> traer u obtener informacion de un atributo
    @property
    def color(self):
        return self.__color
    
    #metodo set -> asigna el valor al atributo
    @color.setter
    def color(self,nuevo_color: str):
        self.__color = nuevo_color


pelotita = PelotaDeJuguete("amarilla")
print("llamado al get de color",pelotita.color)

pelotita.__color= "verde"#no afecta el valor del atributo
print("llamado al get de color",pelotita.color)

#pelotita.color("Azul") no se debe tratar como metodo
pelotita.color = "Azul" #set
print("llamado al get de color",pelotita.color)#get

#pelotita.