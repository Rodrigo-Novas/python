#Programa que calcula perimetro y superficie de un cuadrado circulo rectangulo o triangulo
def cuadrado(lado):
    return[4*lado, lado**2]

def rectangulo(lado_menor, lado_mayor):
    pass
    
def circulo(radio):
    pass
    
def triangulo(base,altura, lado1, lado2):
    pass

print("Perimetro y sup de figuras geometricas", "\n", sep="--------")


while True:
    print("Menu de opciones", sep="--------")
    print("1 Cuadrado", "2 rectangulo", "3 Circulo", "4 Triangulo", "5 Salir", end="\n")
    
    opcion= input("Seleccione una opcion ")
    if opcion == "1":
        lado= float(input("Ingrese lado: "))
        r=cuadrado(lado)
        print(f"El perimetro es{r[0]} y la superficie {r[1]}")
    elif opcion=="2":
        rectangulo(lado_menor, lado_mayor)
    elif opcion=="3":
        circulo(radio)
    elif opcion=="4":
        triangulo(base,altura, lado1, lado2)
    elif opcion=="5":
        print("hasta luego")
        break
    else:
        print("Ingreso mal el numero")
        

    
    