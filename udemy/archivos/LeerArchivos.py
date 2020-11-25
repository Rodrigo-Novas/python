import os


with open("archivo.txt", "w+") as f: #esto en el caso de que este creado lo lee y si no esta creado lo crea con el + tambien se puede escribir
    f.writelines("Hola esto es un archivo por python")
    print(f.readline())
    prit(f.readlines())
# with open("archivo.txt", "x") as f2: #el x si no esta creado lo crea y se esta creado lanza error
#     f2.write("Hola esto es un archivo por python")
#     print(f2.readline())
    
with open("archivo.txt", "a") as f3:#en este caso no crea sino que directamente lo que hace es apendear el texto al final de la linea
    f3.writelines("Hola niños")
    
    
if os.path.exist("archivo.txt"):#si el archivo existe
    os.remove("archivo.txt")#eliminalo, removedir elimina carpetas y rmdir tambien tambien se puede crear con mkdir