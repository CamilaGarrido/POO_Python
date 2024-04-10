class Auto:
    __color = "rojo"

    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor


ferrari = Auto(100)
print(ferrari.valor)