class Pelota():
    def __init__(self) -> None:
        print("Constructor de Clase Pelota")
    
    def imprimir(self):
        imprimir = True
        nombre = input("ingrese su nombre ")
        while imprimir:
            try:
                edad = int(input("ingrese su edad "))
                print("bajo la edad")
                #edad/0
                if edad <= 0:
                    raise EdadError("La edad ingresada no puede ser cero o menor a cero!!!!", edad)

                imprimir = False
            except ValueError:
                print("El dato ingresado no es un numero")
            except ZeroDivisionError:
                print("El divisor no puede ser cero")                
            except EdadError as error:
                print("La edad ingresada no esta correctamente")
pelota_juguete = Pelota()
print(pelota_juguete.imprimir())