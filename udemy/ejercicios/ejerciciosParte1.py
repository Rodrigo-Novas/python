import os

#Multiplicar dos numeros sin usar la multiplicacion


def multiplicarSinMulti(*numArgs):
    cantidad=numArgs[1]
    multi=0
    for x in range(cantidad):
        multi=numArgs[0]+multi
    return multi


#print(multiplicarSinMulti(6,3))


#ingresar apellido y nombre e imprimirlos al reves
def reversear(nombre, apellido):
    concat= f"{nombre} {apellido}"
    print(concat[::-1])
    
#reversear("Rodrigo", "Novas")    

#sacar numero par
def esPar(numero):
    if numero%2==0:
        print("Es par")
    else:
        print("No es par")
        
#esPar(4)

#escribir una funcion que indique cuantas vocales tiene una palabra

def contadorVocales(palabra="murcielago"):
    contadorVoc=0
    for x in range(len(palabra)):
        if palabra[x]== "a" or palabra[x] =="e" or palabra[x]== "i" or palabra[x] =="o" or palabra[x] =="u":
            contadorVoc +=1
    return contadorVoc

#print(contadorVocales())


#Escribir una funcion que pida nombre y apellido y los vaya agregando a un archivo
def nombreApp():
    while True:
        nombre= input("Escribe tu puto nombre: ")
        apellido= input("Escribe tu fucking apellido: ")
        if os.path.exists("archivoNombres.txt"):
            with open("archivoNombres.txt", "a") as f:
                f.writelines(f"{nombre} {apellido}\n")
        else:
            with open("archivoNombres.txt", "w") as f:
                f.writelines(f"{nombre} {apellido}")
        salir= input("Desea seguir ingresando nombres? s")
        if salir.upper() != "S":
            break
            print("Adios")

try:
    nombreApp()
except Exception as ex:
    print("No se pudo realizas", ex)
