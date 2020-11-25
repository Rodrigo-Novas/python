#Juego con input
# dato=input("Ingrese dato: ")
# opciones=["hola", "chancho", "dragones", "perros"]

# if opciones.count(dato)>0:
#     print(f"El dato existe: {dato}")
# else:
#     print(f"El dato no existe: {dato")
class calculadora(object):
    def __init__(self, n1,n2):
        self.n1=n1
        self.n2=n2
        
    def suma(self):
        return self.n1+self.n2
    
    def division(self):
        if n1:
            return self.n1/self.n2
        else:
            return 0
        
    def multiplicacion(self):
        return self.n1*self.n2
    
    def resta(self):
        return self.n1-self.n2
        
if __name__ == "__main__":
    
    try:
        while True:
            n1 = int(input("Ingrese un numero: "))
            n2= int(input("Ingrese otro numero: "))
            calcu= calculadora(n2,n2)
            suma=calcu.suma()
            multi=calcu.multiplicacion()
            div=calcu.division()
            resta=calcu.resta()
            print(f"La suma de los numeros {n1} y {n2} es: {suma}")
            print(f"La multi de los numeros {n1} y {n2} es: {multi}")
            print(f"La div de los numeros {n1} y {n2} es: {div}")
            print(f"La resta de los numeros {n1} y {n2} es: {resta}")
            seguir=input("Desea seguir calculando? s/n ")
            if(seguir.upper()=="N"):
                break
    except Exception as e:
        print(f"Error no es un numero {e}")
        exit()
    finally:
        print("Adios")