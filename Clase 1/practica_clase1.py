"""Crear un bucle que almacene en una variable la suma
de todos los elementos numericos de una lista, a excepcion del ultimo"""

listaNumericos = [1,3,4,5,9]
suma = 0

for idx, j in enumerate(listaNumericos):
    if idx == len(listaNumericos)-1:
        break
    suma = j + suma
    print(idx, j) #imprimo indice valor
    
print(suma)

#Utilizando el for de tipo range
i = 0
suma2 = 0
for i  in range(0,len(listaNumericos),1):
    if i == len(listaNumericos)-1:
        break
    suma2= listaNumericos[i] + suma2
   
print(suma2)


"""Utilizando un bucle “while”, elaborar un código que imprima en pantalla cada uno de los
elementos de una lista y simultáneamente los elimine, hasta quedar vacía."""

listaWhile= ["Jorge", "Ramon", "Alberto", "Pepe"]
indice=0
while True:
    if not listaWhile : #con esto evaluo si la lista es vacia, tambien podria hacer len(listawhile)==0
        print("NADA")
        break
    print(listaWhile[indice])
    listaWhile.pop(indice)
    
    