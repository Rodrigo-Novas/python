import sys

#Esto me sirve para hacer variables de sistema, cuando lo ejecuto en el cmd le paso algo como parametro esto me lo toma

print(sys.argv[0]) #esto lo que me hace es devolver el nombre del programa

nombres = sys.argv[1:] #le saco el indice cero porque va a imprimir el nombre del programaa

if nombres:
    for nombre in nombres:
        print(f"Hola {nombre}")
else:
    print("No me dijiste tu nombre")

# nmap -sS
# argv = ["nmap", "-sS"]