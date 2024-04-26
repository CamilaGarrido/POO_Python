from usuario import Usuario # Importar la clase Usuario desde el archivo usuario.py.
import json  # Importar el módulo json para trabajar con JSON.
from datetime import datetime  # Importar datetime para trabajar con fechas y horas.

# Requerimiento 1: Bloque de código para crear instancias de Usuario.
with open('desafio8/usuarios.txt') as usuarios: 
    #print("line: ",usuarios.readline())
    # Leer línea por línea el archivo usuarios.txt
    linea = usuarios.readline()

    lista_objetos_usuarios = [] # variable de tipo lista para almacenar los objetos.

    while linea: #Agregar en un ciclo.
        try:  #controlar la excepcion
            usuario_dicc = json.loads(linea) #transformar el texto en json.
            #Crear instancia de Usuario
            usuario = Usuario(
                            usuario_dicc['nombre'],
                            usuario_dicc['apellido'],
                            usuario_dicc['email'],
                            usuario_dicc['genero'],
                            )
            lista_objetos_usuarios.append(usuario)
        except Exception as error:
            print(f"el error es:",error) #Imprimir el error
            
            # Requerimiento 2: Manejo de excepciones: imprimir el error y guardarlo en error.log
            now = datetime.now()
            with open(f"{now.strftime('%Y-%m-%d')}_error.log",'a+') as log:
                print(log)
                log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error}\n")
        finally:
            linea = usuarios.readline()
    print("")
    print("contenido de la lista",lista_objetos_usuarios) # Impresión del contenido de la lista con las instancias de Usuario creadas.