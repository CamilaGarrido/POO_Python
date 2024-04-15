class PelotaDePlastico():
    def __init__(self):
        self.rebotes = []

    def rebotar(self, altura):
        print("Clase padre")
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura), 0]
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura):
        print("Clase hija")
        self.rebotes = []
        while altura > 0:
            self.rebotes += [altura, 0]
            altura //= 2

pdj = PelotaDeJuguete()
pdj.rebotar(5)

# Salida: [5, 0, 1, 0]
print(pdj.rebotes)
# Se hace llamado al método del padre PelotaDePlastico
super(type(pdj), pdj).rebotar(5)
# Salida: [5, 0, 2, 0, 1, 0]
print(pdj.rebotes)