def miFuncion(parametro):
    print(f"Esto es mi {parametro}")
    
miFuncion("perro")

#Pasar parametro tipo lista

def miFuncion2(parametroLista):
    print(parametroLista)

lista=["hola", "jose", "lima", "peru"]
miFuncion2(lista)
#miFuncion2("hola", "niños", "peru") esto no funciona porque si no le coloco * antes no interpreta que son multiples

#Pasar mas parametros dentro del scope pero en una sola variable, esto se usa mucho


def miFuncionParametros(*parametrosMultiples): #el * lo que hace es decirle al interprete que es una tupla
        print(parametrosMultiples)
        print(parametrosMultiples[0])#puedo acceder a todos los elementos usando el [0]
        
        
miFuncionParametros("hola", "niños", "peru")


def miFuncionDefecto(nombre="jose", apellido="rodriguez"): #colocarle el = nos da un valor por defecto
        print(nombre + " " + apellido)

miFuncionDefecto()
#acceder a argumentos mediante sintaxys de diccionarios kwargs significa key arguments

def miFuncionDiccionario(**kwargs):
    print(kwargs["nombre"], kwargs["apellido"]) #apellido y nombre son las llaves del diccionario
    

miFuncionDiccionario(nombre="ramon",apellido="villegas")

#recursividad en python, sirve mucho para si queremos hacer barch ej:si queremos que se repita 5o veces y luego otras 50 y asi sucesivamente

def recursion(i):
    if(i<1):
        return i
    else:
        print(i)
    recursion(i-1) #aca llamo a la misma funcion pero esta vez con el valor de n-1
    
recursion(5)