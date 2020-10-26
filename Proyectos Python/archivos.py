import os


if __name__ == "__main__":
    
    def archivos():
        a=True
        if a == True: a=False
        try:
            print("entro")
            f = open("readme.txt", "w+")
          
            while True:
                f.seek(0)
                f.write("holaa niñossss")
                print(f.tell()) #me da la ultima linea
                linea= f.readline()
                if not linea : break                
        except Exception as e:
            print("Usted tiene una excepcion", e)
        finally:
            print("Usted salio")
            f.close()
    archivos()