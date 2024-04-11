import random

class Personaje:
    def __init__(self, nombre):# Constructor de la clase Personaje.Inicializa el nombre, nivel y experiencia.
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def get_estado(self):#Método para obtener el estado actual del personaje.
        return f"Nombre: {self.nombre}, Nivel: {self.nivel}, Experiencia: {self.experiencia}"

    def set_estado(self, experiencia):# Método para asignar un nuevo estado al personaje basado en la experiencia.
        """Si la experiencia es positiva, se aumenta la experiencia y se actualiza el nivel si es necesario.
        Si la experiencia es negativa, se disminuye la experiencia y el nivel si es posible."""
        if 0 <= experiencia <= 99:
            self.experiencia += experiencia
            while self.experiencia >= 100:
                self.experiencia -= 100
                self.nivel += 1
        elif experiencia < 0 and (self.nivel > 1 or self.experiencia > 0):
            self.experiencia += experiencia
            while self.experiencia < 0 and self.nivel > 1:
                self.experiencia += 100
                self.nivel -= 1

    def __lt__(self, otro_personaje):# Método para comparar si un personaje tiene un nivel menor que otro.
        return self.nivel < otro_personaje.nivel
    def __gt__(self, otro_personaje):# Método especial para comparar si un personaje tiene un nivel mayor que otro.
        return self.nivel > otro_personaje.nivel
    def probabilidad_ganar(self, otro_personaje):#Método que calcula la probabilidad de ganar contra otro personaje.
        return 0.33 if self < otro_personaje else (0.66 if self > otro_personaje else 0.5)

    @staticmethod
    def dialogo_enfrentamiento(probabilidad):#Método estático, muestra el diálogo de enfrentamiento con el orco y solicita la opción del jugador.
        print("\n¡Oh no!, ¡Ha aparecido un Orco!\n") # Mostrar información sobre el enfrentamiento con el orco.
        print(f"Con tu nivel actual, tienes {probabilidad*100:.1f}% de probabilidades de ganarle al Orco.\n")
        print("Si ganas, recibirás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        return input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n") # Pedir al jugador que elija una acción.

if __name__ == "__main__": # Crear dos personajes para probar la funcionalidad de la clase Personaje.
    jugador1 = Personaje("Jugador1")
    jugador2 = Personaje("Jugador2")
    probabilidad = jugador1.probabilidad_ganar(jugador2) # Calcular la probabilidad de ganar del primer jugador contra el segundo jugador.
    print(probabilidad)
    print(Personaje.dialogo_enfrentamiento(probabilidad)) # Mostrar el diálogo de enfrentamiento y obtener la opción del jugador.