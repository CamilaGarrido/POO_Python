class Pelota():
    #atributos
    forma = "redondeada"


    #metodo constructor
    """ 
    def __init__(self):
        self.color = "blanco"
        self.tamaño = 10
        self.material = "Plastico"
        print("!Se ha creado una pelota!")
    """
    def __init__(self, color: str,material: str,tamanio=0 ):
        self.color = color
        self.tamanio = tamanio
        self.material = material

        print("!Se ha creado una pelota!")
    
    @property
    def color_y_material(self):
        return f"Pelota {self.color} de {self.material}"
    
    @property
    def colores(self):
        return self.color
    
    @colores.setter
    def colores(self, color: str):
        self.color = color if color != "" else "blanco"

    def getColor(self):
        return self.color

    def setColor(self, value):
        self.color = value


    def __str__(self):
        return f"forma {self.forma},  "
        
        
        
        