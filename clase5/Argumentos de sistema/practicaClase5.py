import shutil as sh
import os
import sys
import subprocess as sb

"""Desarrollar un script buscar_archivos.py que reciba como argumentos la ruta a una
carpeta y una extensión para buscar archivos dentro de ella. Luego debe mostrar los
archivos que terminen con dicha extensión en la carpeta indicada. Por ejemplo, en el caso
siguiente se listan los archivos con extensión “.exe” en la carpeta de instalación de Python:
> python buscar_archivos.py "C:\Python37" .exe
Archivos con extensión .exe:
-> python.exe
-> pythonw.exe"""



def buscarArchivos():
    
    try:
        ruta = sys.argv[1] #ignoro el cero porque es la ruta
        extension= sys.argv[2]
        if os.path.exists(ruta):
            archivos = [i for i in os.listdir(ruta) if i.endswith(extension)]
            print(archivos)
        else:
            print("No existe ruta")
    except Exception as e:
        print(e)
        print("No ingreso el correcto argumento: ")
        

if __name__ == "__main__":
    buscarArchivos()