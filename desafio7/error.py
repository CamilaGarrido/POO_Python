"""Requisito 1: Crear la excepción DimensionError derivada de Exception. 
Sobreescribir el constructor, recibiendo los parámetros mensaje, dimension y maximo, 
y asignándoles los respectivos atributos de instancia. """

class DimensionError(Exception):
    def __init__(self, mensaje="", dimension=None, maximo=None) -> None:
        super().__init__(mensaje)  # Llamar al constructor de la clase base (Exception) con el mensaje proporcionado.
        self.mensaje = mensaje  # Asignar el mensaje proporcionado como un atributo de instancia.
        self.dimension = dimension  # Asignar la dimensión proporcionada como un atributo de la instancia.
        self.maximo = maximo  # Asignar el valor máximo proporcionado como un atributo de la instancia.

    """ Requisito 2: sobrecargar el método __str__, de forma tal que si sólo 
    se ha ingresado mensaje al crear la excepción, se retorna el método de la clase padre. 
    En caso contrario, crear y retornar un mensaje de retorno utilizando los atributos 
    mensaje y/o dimension y/o maximo."""
    
    def __str__(self) -> str:
        if self.dimension is not None and self.maximo is not None:
            return f"Atencion: {self.mensaje}. Debe estar entre 1 y {self.maximo}. Valor ingresado: {self.dimension}." # Si se proporciona dimension y maximo, devuelve un mensaje.
        else:
            return super().__str__()  # Si no se proporcionaron dimension y maximo, devuelve el mensaje de la clase base (Exception).