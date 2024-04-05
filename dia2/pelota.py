class Pelota():
    #atributos
    #pass
    forma = "redondeada"
    posiciones = [3,0,2,1,0]

    #Metodo estatico
    #es invocado sin tener que crear una instancia 
    #no se pueden modificar los atributos
    @staticmethod 
    def crear_rebote():
        posiciones = [5,0,4,0,3,0,2,0,1,0]
        return posiciones

    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)

    #metodo NO ESTATICO
    def rebotar(self):
        #self.posiciones = Pelota.crear_rebote()
        self.posiciones = self.crear_rebote()
        self.forma = "redonda"

    # Método de instancia que asigna color
    def asigna_color(self, nuevo_color: str):
        print(self, type(self))

        self.color = nuevo_color

    # Método de instancia que lee color de la instancia
    def lee_color(self):
        print("El color de esta pelota es {}".format(self.color))

    def lee_color_local_y_atributo(self, color_local: str):
        # Esta variable "color" sólo existe en el alcance del método
        color = color_local
        # Un método de instancia puede llamar a otros métodos
        self.lee_color()
        print("El color {} NO es el color de ESTA pelota".format(color))
    
    def inicia_color(self):
        self.color = ""