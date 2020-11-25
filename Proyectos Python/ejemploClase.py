import re
from app import lista



class instrumento():
    
    def __init__(self, tipo):
        self.tipo = tipo
        
    def tipoInstrumento(self):
        if  self.tipo == "viento":
            return 1
        elif self.tipo=="cuerda":
            return 2
        else:
            return 3
          
    
        
        
        
class Guitarra(instrumento):

    def __init__(self, tipo, cuerdas):
        super().__init__(tipo)
        self.__tipo= tipo #privado      
        self.__cuerdas= cuerdas#privado
        
    def tocar(self):
        for x in range(0,self.__cuerdas,1):
            print("Usted esta tocando", x)
            
    def __str__(self):
        return "Este objeto sirve para poder tener una clase"
 
class fecha(object): #esta es una clase de neuvo estilo que permite usar metodos estaticos, propiedades, descriptores
    def __init__(self, dia):
        self.__dia= dia
        
    def getDia(self):
        return self.__dia
    def setDia(self, dia):
        if self.__dia<=0:
            self.__dia = dia
                        
    dia= property(getDia, setDia) #declaro propiedad


if __name__ == "__main__":
   # print (lista)
    guitarra=Guitarra("viento", 3)

    print(guitarra.tipoInstrumento())
    guitarra.tocar()
    print(guitarra.__str__())
    try:
        fech1= fecha(0)
        print(fech1.getDia())
        fech1.dia= "hola" + 9
        print(fech1.getDia())
    except Exception as e:
        print("Error", str(e))
    finally:
        print("Adios")

    print(re.match(".ython", "python"))

    

