class Vehiculo():
    def __init__(self, nombre: str = ""):
        self.nombre = nombre

    def cant_ruedas(self):
        pass

class Bus(Vehiculo):#herencia
    def __init__(self, nombre: str = ""):
        super().__init__(nombre)#constructor clase padre(Vehiculo)
        self.num_pasajeros=0

    def cant_ruedas(self):
        return 6

class Auto(Vehiculo):#herencia
    def __init__(self, nombre: str = ""):
        super().__init__(nombre)

    def cant_ruedas(self):
        return 4 

#instancia de clase Bus
bus = Bus("BioBio")
print(bus.cant_ruedas())
print(bus.nombre)