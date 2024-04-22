import os

#manipular un archivo
log_file1 = open(os.path.abspath("dia11/logs/error.log"),'r')

#FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Talento digital\\2023\\0044-2\\MODULO_POO\\logs\\error.log'

#FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Talento digital\\2023\\0044-2\\MODULO_POO\\dia11\\logs\\error.log'
#PS C:\Talento digital\2023\0044-2\MODULO_POO> 

#r abierto para la laectura
#Lectura de un archivo existente.
log_file2 = open(os.path.abspath("dia11/index.html"),'r')
#leer el contenido de un archivo.
print(log_file2.read())
print("****************************")
print(log_file2.readlines())
print("****************************")
with open(os.path.abspath("dia11/index.html"),'r') as archivo:
    for linea in archivo:
        print(linea.strip())










