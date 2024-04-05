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