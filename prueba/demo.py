from campania import Campania, LargoExcedidoException # Importar la clase Campania y la excepción LargoExcedidoException desde el módulo campania.
from error import SubTipoInvalidoException # Importar la excepción SubTipoInvalidoException desde el módulo error.
from anuncio import Video # Importar la clase Video desde el módulo anuncio.
from datetime import datetime # Importar la clase datetime desde el módulo datetime.

# Paso 1: Crear una instancia de Campania con un anuncio de tipo Video.
fecha_inicio = datetime(2024, 4, 30) # Definir las fechas de inicio 
fecha_termino = datetime(2024, 5, 30) #y fin de la campaña.

# Paso 2: Crear un anuncio de tipo Video con sus atributos.
ancho_video = 1280
alto_video = 720
url_archivo_video = "video.mp4"
url_clic_video = "url_clic"
sub_tipo_video = "instream"
duracion_video = 30
anuncio_video = Video(ancho_video, alto_video, url_archivo_video, url_clic_video, sub_tipo_video, duracion_video)

nombre_campania = "Campaña de prueba" # Crear la campaña con el nombre y los anuncios definidos.
campania = Campania(nombre_campania, fecha_inicio, fecha_termino, [anuncio_video])

# Paso 3: Manejar excepciones al intentar modificar el nombre de la campaña.
try:
    nuevo_nombre = input("Ingrese el nuevo nombre para la campaña: ")
    campania.modificar_nombre(nuevo_nombre)  # Se intenta modificar el nombre de la campaña.
except LargoExcedidoException as e:
    with open("error.log", "a") as file:
        file.write(f"{str(e)}\n")  # Si se excede el largo, se escribe en el archivo de error.log.
    print(str(e))  # imprimir mensaje de error en la terminal.
except FileNotFoundError:
    print("No se encontró el archivo de registro de errores.")  # Mensaje si el archivo de registro no se encuentra.
else:
    try:
        subtipos_validos = ["instream", "outstream"]
        print(f"Ingrese el nuevo subtipo para el anuncio ({'/'.join(subtipos_validos)}): ")
        nuevo_sub_tipo = input()

        # Paso 4: Validar el subtipo ingresado para el anuncio de video.
        if nuevo_sub_tipo not in subtipos_validos: # Validar que el subtipo ingresado sea uno de los subtipos válidos.
            raise SubTipoInvalidoException(f"El nuevo subtipo no es válido para este tipo de anuncio.")
        anuncio_video.modificar_subtipo(nuevo_sub_tipo)  # Se intenta modificar el subtipo del anuncio de video.
    except SubTipoInvalidoException as e:
        with open("error.log", "a") as file:
            file.write(f"{str(e)}\n")  # Si se produce una excepción por subtipo inválido, se escribe en el archivo de error.log.
        print(str(e))  # imprimir el mensaje de error en la terminal.
    else:
        # Paso 5: Mostrar información de la campaña solo si no hay errores.
        print(f"Nombre de la campaña: {campania._Campania__nombre}")
        print(f"Fechas: Desde {fecha_inicio.strftime('%Y-%m-%d')} hasta {fecha_termino.strftime('%Y-%m-%d')}")
        print("Anuncios:", campania.anuncios_str())
        print("No se encontraron errores en el archivo de registro.")