import clase3
class excepcionNumeros(Exception):
    
    def __init__(self, mensaje):
        super(excepcionNumeros, self).__init__(mensaje) 

def suma(n):
    if not isinstance(n, (int,float)):
        raise excepcionNumeros("Error esto no es numero")
    else:
        return n+n

if __name__ == "__main__":
     
    f=input("Ingrese un numero ")
    try:
        suma=suma(f)
    except Exception as e:
        print(e)