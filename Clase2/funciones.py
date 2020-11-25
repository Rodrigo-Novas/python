
def f():
    pass

def sumar (a,b):
    """Funcion que retorna la suma de los numeros"""
    return a+b
 
def imprimir_mensaje(mensaje="Pasame un mensaje"):
    print(mensaje)

sumar2 = lambda a,b : a+b


print(sumar2(5,4))
print(sumar(2,3))
print(help(sumar) #el help lo que hace es tirarte el docstring de la funcion
imprimir_mensaje("Hola a todos")

