import random
from personaje import Personaje  # Importa la clase Personaje desde el archivo personaje.py.

class Juego:
    def __init__(self):
        pass
    def jugar(self): # Función para mostrar el estado actual de los personajes.
        def mostrar_estado(jugador, orco):
            print(f"NOMBRE: {jugador.nombre} NIVEL: {jugador.nivel} EXP: {jugador.experiencia}")
            print(f"NOMBRE: {orco.nombre} NIVEL: {orco.nivel} EXP: {orco.experiencia}\n")

        jugador = Personaje(input("¡Bienvenido a Gran Fantasía!\nPor favor, indique el nombre de su personaje: ")) # Crear el personaje del jugador.
        print(jugador.get_estado()) # Mostrar el estado inicial del jugador.
        orco = Personaje("Orco")# Crear un personaje orco.
        while True:
            probabilidad = jugador.probabilidad_ganar(orco) # Calcular la probabilidad de ganar contra el orco.
            print("\n¡Oh no!, ¡Ha aparecido un Orco!\n") # Mostrar información sobre el enfrentamiento con el orco.
            print(f"Con tu nivel actual, tienes {probabilidad*100:.1f}% de probabilidades de ganarle al Orco.\n")
            print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
            print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n")
            opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n") # Pedir al jugador que elija una acción.

            if opcion == "1": # Opcion de atacar.
                resultado = "Gana" if random.uniform(0, 1) <= probabilidad else "Pierde" # Calcular el resultado del ataque.
                if resultado == "Gana":#Si el jugador gana
                    print("\n¡Le has ganado al orco, felicidades!")
                    print("¡Recibirás 50 puntos de experiencia!\n")
                    jugador.set_estado(50)  #Actualizar el estado del jugador.
                    orco.set_estado(-30)  #Actualizar el estado del orco.
                else:  # Si el jugador pierde
                    print("\n¡Oh no! ¡El orco te ha ganado!")
                    print("¡Has perdido 30 puntos de experiencia!\n")
                    jugador.set_estado(-30) #Actualizar el estado del jugador.
                    orco.set_estado(50) #Actualizar el estado del orco.
                mostrar_estado(jugador, orco) #Mostrar el estado actualizado de los personajes.

            elif opcion == "2":  # Opción de huir.
                print("\n¡Has huido! El orco ha quedado atrás.")
                break #Terminar el juego.
            else:  
                print("\nPor favor, selecciona una opción válida (1 para Atacar, 2 para Huir).\n")# Opción inválida.
if __name__ == "__main__":
    Juego().jugar()# Iniciar el juego.