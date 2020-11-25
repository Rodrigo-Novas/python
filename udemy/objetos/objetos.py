import string

#Clases y objetos
class Usuario(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def __str__(self):
        return f"Soy un usuario y mis datos son: {self.getApellido()}  {self.getNombre()}" #funciona perfecto
class Admin(Usuario):
    def __init__(self, nombre, apelldio):
        super().__init__(nombre, apellido) #hago referencia al padre
      
if __name__ == "__main__":
    nombreUser= input("Ingrese nombre: ")
    apellidoUser= input("Ingrese apellido: ")
    user= Usuario(nombreUser, apellidoUser)
    print(user)
    del user #es un destructor elimina el objeto

