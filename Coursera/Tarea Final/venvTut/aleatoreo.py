import random as r
import time

class dados():
    def __init__(self):
        self.random=[]
        self.suma=0

    #declare list and get random numbers 
    def tirar_Dados(self):
        """TIra los dados de forma aleatorea rango del 1 al 6"""
        
        self.random = [r.randint(1, 6)  for n in range(2)]
        print (self.random)
        for i in range(len(self.random)):
            self.suma= self.random[i]+ self.suma
        print(self.suma)


def main():
    """Ejecuta la clase dado """
    dados1= dados()
    while(True):
        
        print("Bienvenido")        
        s=input("Desea tirar nuevamente un dado un nuevo dado? S para tirar ")
        if(s.casefold()=='s'):
            dados1.tirar_Dados()
        else:
            print("Adios")
            time.sleep(1)
            break
            
            
#Esto es para test
if __name__ == "__main__":
    main()


