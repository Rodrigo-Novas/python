import ejecuto_miExcepcion as e


try:
    numero = int([1,2,3,4])
except Exception as e:
    print(f"Esto es una excepcion {e}")
else:
    print("Esto es una lista")
finally:
    print("Adios")
    
    
    
def sumar(a,b):
    if not isinstance(a, (int,float)) or not isinstance(b,(int,float)): #is isntance es mucho mas recomendable usarlo que el type(a)
        raise TypeError("Se requieren dos numeros")
    else:
        return a + b
     



