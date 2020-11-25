import sys
import os


#python buscar archivos.py "c:\\user\\usuario\\pictures" ".jpeg"

while true:
    if len(sys.argv) != 3:
        print("""Error
              EJ DE USO: pYTHON BUSCAR_ARCHIVOS.PT "C\\USERS\\USUARIO\\PICTURES' '.JPEG'""")
        sys.exit()
    
ruta, extension = sys.argsv[1], sys.argv[2]


if not os.path,exists(ruta):
    print("No existe la ruta")
    sys.exit() #cierra el programa

if extension.startswith(".")
    extension = extension.replace(".", "")
    
for archivo in os.listdir(ruta):
    cadena=[]
    cadena=archivo.split(".")
    if len(cadena) < 2:
        continue
    if cadena[1] == extension:
        print(archivo)