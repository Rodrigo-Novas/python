import os

"""
Programa que lea un archivo con temperaturas en °c y genere otro archivo con las temp equivalentes
pero en °F genere el archivo de entrada y denominelo "centigrados.txt"
"""


def archivoGradosCelsius():
    """Crea y/o escribe un archivo con grados celsius"""
    
    grados = ["10°C\n", "12.5°c\n", "16°C\n", "13°c\n","9°C\n", "50°c\n", ]
    if os.path.exists("centigrados.txt"):    
        with open("centigrados.txt", "a") as f:
            f.writelines(grados) #write lines escribe una linea, esas lineas se pasan en forma de lista
    else:
        with open("centigrados.txt", "w") as f:
            f.writelines(grados) 
                      
    with open("centigrados.txt", "r") as f:
        lineas = f.readlines()
        archivoGradosFarenheit(lineas)

        
        
        
def archivoGradosFarenheit(lineas):
    """Realizo archivo grados farenheit"""
    if os.path.exists("farenheit.txt"):    
        with open("farenheit.txt", "a") as f:
            for linea in lineas:
                temp, escala = linea.split("°") #divido en lista el texto y hago un decouple
                temp = float(temp) *1.8 + 32
                f.write("{:.2f}°F\n".format(temp))#el : indica que vamos a formatear lo que esta despues y el . indica que va a ser el decimal en este caso le digo que muestre dos digitos despues de la coma (No funciona con la foma corta)
    else:
        with open("farenheit.txt", "w") as f:
            for linea in lineas:
                temp, escala = linea.split("°") #divido en lista el texto y hago un decouple
                temp = float(temp) *1.8 + 32
                f.write(f"{temp}°F\n")
                  
         

if __name__ == "__main__":
    archivoGradosCelsius()
    
