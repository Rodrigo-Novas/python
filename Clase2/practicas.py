import os
import re



"""En matemática, se conoce a la “sucesión de Fibonacci” como una sucesión infinita de
números naturales en la que cada término está determinado por la suma de los dos
términos anteriores. Por ejemplo, empezando con el 0 y el 1, los primeros 20 términos son
los siguientes:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
1597, 2584, 4181
Crear una función en Python que tome como argumento un entero que indique la cantidad
de términos y retorne una lista como la anterior. Por ejemplo:
>>> fib(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
La función debe, además, chequear que el argumento pasado sea mayor a 2. En caso de
ser menor, debe mostrar un mensaje en pantalla y no retornar nada.
>>> fib(1)
La cantidad debe ser mayor a 2."""



#Fibonacci

def fib(num):
    mensaje_error="La cantidad debe ser mayor a 2"
    lista= []
    sumaLista=[]
    suma=0 
    if num==2:
        return mensaje_error
    for i in range(0,num,1):
        lista.append(i)
    for j in range(0,num,1):
        if(j!=0 and j!=1):
            suma =  sumaLista[j-2] + sumaLista[j-1] 
            sumaLista.append(suma)
        elif (j==0):
            sumaLista.append(0)
        elif (j==1):
            sumaLista.append(1)
            
    return sumaLista


"""Escribir una función que, dado un número máximo, retorne una lista con todos los números
desde 1 hasta dicho número que sean simultáneamente múltiplos de 3 y de 5 (usar la
operación resto con el carácter %)."""
#Multiplos
def multiplos(numMax):
    lista=[]
    for i in range(1,numMax+1):
        if (i % 3 == 0 and i % 5==0):
            lista.append(i)
    return lista


if __name__ == "__main__":
    #fib(30)
    print(multiplos(30))