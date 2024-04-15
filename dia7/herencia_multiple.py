########################################################
class Padre():
    tipo = "Papa"

    def __init__(self, color: str,**parametros):
        super().__init__(**parametros)
        self.color = color #"Rojo"
    
    def imprimir(self):
        print("este metodo pertenece a la clase Padre")

########################################################
class Madre():
    tipo = "Mama"

    def __init__(self, tamanio: str, **parametros):
        super().__init__(**parametros)
        self.tamanio = tamanio
    def imprimir(self):
        print("este metodo pertenece a la clase Madre")

########################################################
class Hijo(Madre,Padre):
    #sobreescritura de los constructuctores
    """
    def __init__(self, tamanio: str, color:str):
        Madre.__init__(self,tamanio)
        Padre.__init__(self,color) 
    """
    def __init__(self, **parametros):
        super().__init__(**parametros)

#hijito = Hijo("Medium","Cafe")
hijito = Hijo(tamanio = "Medium",color="Cafe")
#print(hijito.color,hijito.tamanio)#AttributeError: 'Hijo' object has no attribute 'color'
print(hijito.tamanio)

hijito.color= "Blanco"
hijito.tamanio= "XL"
print(hijito.color,hijito.tamanio, hijito.tipo)

hijito.imprimir()

#isinstance
print(isinstance(hijito,Madre), isinstance(hijito,Padre))