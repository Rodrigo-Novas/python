#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

"""
Comentario 
Multilinea
"""
'''
otro
comentario multilinea
'''

saludo= "hola"
a=1
nombre= input("Ingrese nombre \n")
edad=int(input("Ingrese edad \n"))

print("Hola ", nombre, "Parece que tuviera", edad*2)


if edad>=18:
    print("Usted es mayor de edad")
elif edad >=15 and edad <=18:
    print("Es adolescente")
else:
    print("Usted es niño")
    
#While
i=0
notas =[10,30,50,40]
alumnos =["Rodrigo", "Victor", "Ana"]
while i<len(alumnos):
    print(alumnos[i])
    i += 1
    


#formato de prints
while True:    
    a= 3
    b = 4
    print(f"LA SUMA ENTRE {a} {b} es {a + b}") #para formatear la cadena me permite hacer string interpolate
    print(r"Hola \n")
    opcion = input("Desea Salir? s/n")
    if opcion.casefold() == "s":  #si uso opcion.capitalize() la pasa a upper case, casefold la pasa a lower
        print("Hasta Luego")
        break

#alumnos

for alumno in alumnos:
    print(alumno)

for nota in notas:
    print(nota)
    
for caracter in "HOLA A TODOS":
    print(caracter, end="**") #el end lo que hace es ponerle un separador a cada letra sino por defecto le hace /n
    
for i in range(0,11,1): #Esto simula un for normal
    print(i, i**2)
     
    
    