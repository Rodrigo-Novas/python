#Programacion funciona


"""La programacion Funcional es un paradigma en el que la progrmacin
se basa casi en su totalidad en FUNCIONES, entendiendo el condepto de funcion
segun su definicion matematica y no como los simples subprogramas de los lenguajes
imperativos"""


#Funciones de orden superior

"""El concepto de funciones de orden superior se refiere al uso de funciones como si de un
valor cualquiera se tratara, posibilitando el pasar funciones como parametros de otras funciones o devolver funciones
como valor de retorno las funciones en python son objetos"""


def saludar(lang): #creo funcion que contiene otras funciones
    def saludar_es():
        print ("Hola")
    def saludar_en():
        print ("Hi")
    def saludar_fr():
        print ("Salut")
       
    lang_func = {"es": saludar_es, "en" : saludar_en, "fr": saludar_fr} #creo diccionario que carga las subfunciones en las key como valor
    return lang_func[lang] #retorno el valor que corresponde a la key es


f = saludar("es") #le paso la clave
f() #con esta sentencia lo que hago es ejecutarla

#iteraciones de orden sobre listas

"""Una de las cosas mas interesantes que se pueden hacer
con nuestras funciones de orden superior es pasarlas como argumentos de las funciones 
map, filter y reduce, estas funciones nos permiten sustitutir los bucles tipicos de los lenguajes
 imperativos mediantes construcciones equivalentes"""

#map(function, sequence[,ssequence,...])
"""La funcion map aplica una funcion a cada elemento de una secuencia y devuelve una lista
con el resultado de aplicar la funcion a cada elemento. Si se pasan como parametros n secuencias, 
la funcion tendra que aceptar n argumentos si alguna de las secuencias es mas pequeña que las demas, 
el valor que le llega a la funcion function para posiciones mayores que el tamaño de dicha secuencia sera none"""


#En este ejemplo podemos ver que se utiliza map para elevar al cuadrado todos los elementos de una lista

def cuadrado(n):
    return n**2
l=[1,2,3]
l2 = map(cuadrado, l) #en este caso aca aplica una secuencia a cada uno de los elemento
print(*l2) #el * lo que hace es iterar la lista sin usar el for


# Filter(function, sequence)

"""La funcion filter verifica que los elementos de una secuencia cumplan una determianda condicion, 
devolviendo una secuencia con los elementos que cumplen esa condicion. Es decir para cada elemento de sequence se aplica
la funcion function; si el resultado es true se añade a las lista y en caso contrario se descarta"""

#En este ejemplo se ve el uso de filter para conservar los numeros que son pares

def es_par(n):
    return (n % 2.0 == 0)
l=[1,2,3]
l2 = filter(es_par, l)
print(*l2)

# Reduce(function, sequence[, initial])

"""La funcion reduce aplica una funcion a pares de elementos de una secuencia hasta dejarla en un solo valor"""

#En el ejemplo reduce se usa para sumar todos los elementos d euna lista, esta deprecada

"""def sumar(x, y):
    return x + y

l= [1, 2, 3]
l2=reduce(sumar,l)
print(l2)"""

#Funciones Lambda

"""El operador lambda se utiliza para crear funciones anonimas. Las funciones anonimas al no contener nombre
no pueden referenciarse posteriormente, sirven para ahorrar lineas de codigo """

#Ejemplo lambda

l=[1,2,3]

l2= filter(lambda n: n % 2.0 ==0, l) #la estructura de lambda es (parametros, codigo de la funcion)

#Comprension de listas

"""En python 3000 las funciones map, filter y reduce van a dejar de usarse y se usara list comprehension como 
se usa en haskell"""

"""Estas constan de el parametro que le envias y las operaciones que queres realizar"""

#En este ejemplo se utiliza un for para iterar cada elemto, lo que hace es elevar al cuadrado cada elemento de la lista
l= [0,1,2,3]
l2= [n**2 for n in l]

#Generadores

"""Los generadores son funciones especiales que genera valores sobre los que iterar. Para devolver 
el siguiente valor sobre el que iterar se utiliza ala palabra clave yield en lugar de return. Es la misma
sintaxys que la list comprehension"""


def mi_generador(n,m,s):
    while(n<=m):
        yield n 
        n+=s

"""Se pueden utilizar en cualquier lugar donde se necesite un objeto iterable por ejemplo en un for in"""
for n in mi_generador(0,5,1):
    print(n)
    



