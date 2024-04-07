from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipo_masa #Importar las listas de ingredientes desde el archivo ingredientes.py.

#Requerimiento 1: Definir Clase Pizza con atributos de clase.
class Pizza:
    def __init__(self):#En el método de inicialización (init), se establecen los atributos de la pizza.
        self.ingrediente_proteico = None
        self.ingrediente_vegetal_1 = None
        self.ingrediente_vegetal_2 = None
        self.tipo_masa = None
        self.tamaño = "Familiar"  #tamaño de la pizza por defecto.
        self.precio = 10000  #precio de la pizza por defecto.
        self.es_valida = False

    #Requerimiento 2: Método (estático) para validar un elemento dentro de una lista.
    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    #Requerimiento 3: Método para que el usuario haga su pedido.
    def realizar_pedido(self):
        print("¡Bienvenido a la pizzería! ¿Listo para armar tu pizza?\n")# Mensaje de bienvenida.
        # Solicitar al usuario seleccionar los ingredientes y el tipo de masa.
        self.ingrediente_proteico = self.solicitar_opcion(ingredientes_proteicos, "Por favor, seleccione su opción de proteína:")
        self.ingrediente_vegetal_1 = self.solicitar_opcion(ingredientes_vegetales, "Por favor, seleccione su opción de primer vegetal:")
        self.ingrediente_vegetal_2 = self.solicitar_opcion(ingredientes_vegetales, "Por favor, seleccione su opción de segundo vegetal:")
        self.tipo_masa = self.solicitar_opcion(tipo_masa, "Por favor, seleccione su opción de tipo de masa:")

        self.es_valida = self.validar_pedido() # Validar el pedido
    def solicitar_opcion(self, opciones, mensaje):# Solicitar al usuario que elija entre las opciones proporcionadas.
        print(mensaje)
        for i, opcion in enumerate(opciones, start=1):
            print(f"\t{i}. {opcion}")
        while True:
            opcion = input("\nIngrese el número correspondiente a su elección: ")
            try:
                opcion_numero = int(opcion)
                if 1 <= opcion_numero <= len(opciones):
                    return opciones[opcion_numero - 1]
                else:
                    print("Opción inválida. Por favor, ingrese un número válido.")
            except ValueError:
                print("Opción inválida. Por favor, ingrese un número válido.")

    #Requerimiento 4: Validar el pedido.
    def validar_pedido(self):
        proteico_valido = self.validar_elemento(self.ingrediente_proteico, ingredientes_proteicos)
        vegetal_1_valido = self.validar_elemento(self.ingrediente_vegetal_1, ingredientes_vegetales)
        vegetal_2_valido = self.validar_elemento(self.ingrediente_vegetal_2, ingredientes_vegetales)
        masa_valida = self.validar_elemento(self.tipo_masa, tipo_masa)
        return proteico_valido and vegetal_1_valido and vegetal_2_valido and masa_valida

    def mostrar_pedido(self):#mostrar el pedido realizado por el usuario.
        print("\nDetalle del pedido:")
        print("Ingrediente proteico:", self.ingrediente_proteico)
        print("Ingredientes vegetales:", self.ingrediente_vegetal_1, "y", self.ingrediente_vegetal_2)
        print("Tipo de masa:", self.tipo_masa)
        print("Tamaño de la pizza:", self.tamaño)
        print("Precio de la pizza:", self.precio)
        print("¿Es un pedido de pizza válido?", "Sí" if self.es_valida else "No")

if __name__ == "__main__":
    pizza = Pizza() # Crear una instancia de la clase Pizza.
    pizza.realizar_pedido() # El usuario realiza su pedido.
    if pizza.es_valida:
        pizza.mostrar_pedido()# Mostrar el pedido realizado por el usuario.
        print("\n¡Gracias por tu pedido! ¡Vuelve pronto!")# Mensaje de despedida.
    else:
        print("Pedido no válido. Por favor, ingrese valores válidos.")