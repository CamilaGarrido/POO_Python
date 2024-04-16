# Paso 1: Definir la clase abstracta base para todas las membresías.
from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo: str, numero_tarjeta: str):
        self._correo = correo
        self._numero_tarjeta = numero_tarjeta

    @property
    def correo(self):
        return self._correo

    @property
    def numero_tarjeta(self):
        return self._numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia):
        pass

    @abstractmethod
    def cancelar_suscripcion(self):
        pass

# Paso 2: Definir la clase para la membresía gratuita.
class Gratis(Membresia):
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia == 1:
            return Basica(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self._correo, self._numero_tarjeta)
        else:
            return self

    def cancelar_suscripcion(self):
        return Gratis(self._correo, self._numero_tarjeta)

# Paso 3: Definir la clase para la membresía básica.
class Basica(Membresia):
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia == 1:
            return Basica(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self._correo, self._numero_tarjeta)
        else:
            return self

    def cancelar_suscripcion(self):
        return Gratis(self._correo, self._numero_tarjeta)

# Paso 4: Definir la clase para la membresía familiar.
class Familiar(Membresia):
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia == 1:
            return Basica(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self._correo, self._numero_tarjeta)
        else:
            return self

    def cancelar_suscripcion(self):
        return Gratis(self._correo, self._numero_tarjeta)

# Paso 5: Definir la clase para la membresía sin conexión.
class SinConexion(Membresia):
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia == 1:
            return Basica(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self._correo, self._numero_tarjeta)
        else:
            return self

    def cancelar_suscripcion(self):
        return Gratis(self._correo, self._numero_tarjeta)

# Paso 6: Definir la clase para la membresía pro.
class Pro(Membresia):
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia == 1:
            return Basica(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self._correo, self._numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self._correo, self._numero_tarjeta)
        else:
            return self

    def cancelar_suscripcion(self):
        return Gratis(self._correo, self._numero_tarjeta)
#Ejemplo.
if __name__ == "__main__":
    membresia_actual = Gratis("ejemplo@gmail.com", "123456789")
    print("Tipo de membresía actual:", type(membresia_actual).__name__)

    nueva_membresia = membresia_actual.cambiar_suscripcion(3)
    print("Nuevo tipo de membresía:", type(nueva_membresia).__name__)

    nueva_membresia = nueva_membresia.cambiar_suscripcion(2)
    print("Nuevo tipo de membresía:", type(nueva_membresia).__name__)

    nueva_membresia = nueva_membresia.cambiar_suscripcion(1)
    print("Nuevo tipo de membresía:", type(nueva_membresia).__name__)

    nueva_membresia = nueva_membresia.cambiar_suscripcion(4)
    print("Nuevo tipo de membresía:", type(nueva_membresia).__name__)

    membresia_cancelada = nueva_membresia.cancelar_suscripcion()
    print("Nuevo tipo de membresía:", type(membresia_cancelada).__name__)