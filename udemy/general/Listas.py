lista =[1,2,3]
lista2=[]
lista2= lista #aca si borro la lista principal directamente se me elimina esta tambien, todo cambio que hago en la principal afecta a esta
lista2= lista.copy() #esta lo que hace es hacer la copia de una etapa en especifico, por lo tanto si borro despues la lista principal esta no se ve afectada
#print(lista2)
lista.append(4)
lista.clear()
#print(lista2)
print(lista2.count(3)) #count lo que hace es contar la cantidad de veces que se repite un item en una lista
print(len(lista2)) #len me cuenta los elementos
print(lista2[0:3])#slicing del cero al 3
print(lista2[0])#primer elemento
lista2.pop(0) #pop elimina el ultimo elemento de la lista, por defecto si lo dejo sin indice elimina el ultimo elemento
del lista2[0] #tambien elimina el 
print(lista2[0])
lista2.remove(3) #elimina un elemento por su valor no por su indice, en este caso eliminaria el ultimo elemento
lista2.sort()#el sort ordene por un parametro, si o si los elemento de la lista que ordeno deben ser del mismo tipo (ej todas string o todas enteros)
lista2.reverse()#el reverse da vuelta una lista
print(lista2.index(3)) #te devuelte el indice por el valor que le pasas por parametro
tupla=("niños","hola")
lista_tupla=list(tupla) #con esto casteo la tupla y la convierto a lista