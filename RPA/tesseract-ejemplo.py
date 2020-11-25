import pytesseract as tsc
import time 
import os
#tesseract detecta el texto principal
tsc.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Con esto lo que logro es cambiar el path a donde yo lo tengo instalado
ruta= r"C:\\Users\\novasrodrigo\\Desktop\\Curso python\\Tesseract placas"
archivos = os.listdir(ruta) #lista los archivos del directorio

for elemento in archivos:
    if elemento.split(".")[-1] in ("png", "jpg", "jpng", "tiff"): #lo que hace el -1 es agarrar el ultimo elemento de la lista
        texto= tsc.image_to_string(ruta + "\\" + elemento, config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890') #el config es una configuracion especial siempre usar esta mejora la deteccion
        print(texto)


