"""En las funciones hago el raise y en el main hago el try except"""

def suma(a,b):
    return a+b


def resta(a,b):
    return a-b


def multiplicador(a,b):
    return a*b



def division(a,b):
    if b:  #es lo mismo que hacer b!=0 porque por defecto si es negativo o cero lo que hace es devolver false
        return a/b
    else:
        raise ZeroDivisionError #lanzo la excepcion
    
    
    





