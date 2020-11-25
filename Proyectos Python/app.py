#declaracion de  variables

cadena = r"hola \n f" #raw sirve para expresiones regulares
cadenaTripleComilla= """hola sirvo para hacer
                        saltos de linea"""
                        
lista= [33,"roberto", "cachanosky", 3.12] #declaro list 1

print(lista[0:3]) #imprimo lista1

lista2= lista[0:2] #declaro e incializo con los datos de list1 a lista 2

print(lista2)
lista[0:2]=[] #elimino los elementos de lista1

print(lista)

#lista compuesta

listaComp =[1,True, [0,4]]

print(listaComp[2][1])

#imprimir lista de forma contraria (al reves)

print(lista[-1]) #esto imprime el ultimo elemento

#Tuplas (son inmutables y de tamaño fijo pero mas ligeras que las listas)
tupla= (1,) #tupla de un solo elemento siempre lleva coma
tupla2=(3, True, False, "roberto") #tupla normal
''' esto es un comentario multilinea'''
print (cadena)
print (cadenaTripleComilla) 
