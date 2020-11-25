import sys
import os
import shutil #shutiil sirve como os para gestionar archivos
import subprocess #nos permite ejecutar procesos de cmd desde python
"""
El modulo de sys nos permite pasarle argumentos al programa y convertirlo en ejecutable, nos permite realizar scripts.
Dichos argumentos se especifican luego del nombre del programa y separados por espacios.

Supongamos que tenemos un archivo llamado saludar.py y que lo ejecutamos desde la
terminal del siguiente modo:
> python saludar.py Lautaro

"""

# 
# C:\Users\novasrodrigo\Desktop\data science>python argumentosDeSystema.py Rodrigo
# argumentosDeSystema.py
# argumentos ['argumentosDeSystema.py', 'Rodrigo']
# 


try:   
    print(sys.argv[0]) #el argumento cero lo que hace es pasar la ruta del archivo
    print(sys.argv[1]) #esto devuelve el primer parametro que ingresas por consola
    print("argumentos", sys.argv)
except Exception as e:
    print("no ingresaste un parametro")
finally:
    print("Adios")



# Usamos la propiedad de «slicing» para ignorar el primer
# argumento, i. e. el nombre del programa.
nombres = sys.argv[1:]
# # Chequeamos que la lista no esté vacía.
if nombres:
    for nombre in nombres:
        print(f"¡Hola, {nombre}!")
else:
    print("No has indicado ningún nombre.")



# ¿Cómo deberíamos invocar este programa? Así:
# > python saludar.py Lautaro José Sofía
# Y el resultado en pantalla es:
# ¡Hola, Lautaro!
# ¡Hola, José!
# ¡Hola, Sofía!



#Gestion de archivos!!!!!!!!!11

#De os nos interesan estos archivos

# ● os.listdir() #este nos devuelve la lista de directorios de la ruta en donde estamos
# ● os.getcwd()  este nos devuelve la ruta del archivo  
# ● os.mkdir()
# ● os.path.exists()
# ● os.rename()
# ● os.remove()
# ● os.rmdir()



# Por otro lado, dentro del módulo shutil nos interesan las siguientes:
# ● shutil.copy() #copia un archivo a otro lado
# ● shutil.move() #como el copy pero lo corta
# ● shutil.rmtree() #este lo que hace es eliminar los archivos y carpetas dentro de la carpeta que le indiquemos



#Subprocesos


# Una tarea frecuente en el desarrollo de scripts es la de tener que invocar un programa o
# comando del sistema desde Python, y ocasionalmente leer el resultado que imprime en
# pantalla. Para ello la librería estándar provee el módulo subprocess.
# Por ejemplo, supongamos que queremos ejecutar el siguiente comando de Windows que
# crea una nueva carpeta en la ruta desde donde se esté ubicado en la terminal:
# > mkdir nueva_carpeta


subprocess.run(["mkdir", "nuevaCarpeta"], shell=True)


# Probemos ahora un comando que imprima información en la consola y queramos analizar
# desde Python. Por ejemplo, hostname, que indica el nombre del host actual, o whoami,
# que imprime el nombre del host y el del usuario.
# > hostname
# DESKTOP-JL5G5BG
# > whoami
# desktop-jl5g5bg\usuario


subprocess.run("hostname", capture_output=True ,encoding="cp850", )

# ● El primer argumento es una cadena y no una lista. Esto es válido porque el comando
# no contiene espacios, entonces, se puede pasar directamente una cadena.
# ● El argumento capture_output=True le indica a la función run() que debe
# capturar el resultado del comando (esto es, el nombre del host).
# ● El argumento encoding="cp850" indica la codificación de caracteres usada por
# defecto por la consola de Windows. No es relevante en este momento, simplemente
# recuerda usarlo tal como lo hemos hecho recién siempre que quieras leer el
# resultado de un comando desde Python.
# ● No especificamos el parámetro shell=True. Esto es porque hostname es en
# realidad un programa, no un comando. Podemos observar esto escribiendo where
# hostname en la consola, lo cual nos revelará la ubicación del programa (por lo
# general, C:\Windows\System32\HOSTNAME.EXE). Siempre que ejecutemos un
# programa en lugar de un comando debemos evitar el parámetro shell.
