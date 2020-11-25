x = 1+4*3+8/2*4+5**2

print(x + 1 if x % 2==0 else x + 2)

#lambda

f = lambda x: x+1

print(f(5))


#fibonnacci
#lista
x=35
g=35
def fib(x):
    fibonnacci = []
    for i in range(0,x+1,1):
        fibonnacci.append(i)
    
    print(*fibonnacci)    
    for n in range(0,x+1,1):
        if (n>=1):
            numero= fibonnacci[n] + fibonnacci[n-1] 
            print(numero)
    return numero

def fib2(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
        print(f1,f2)
    return f1

print(fib2(g))
print(fib(x))
print(list(range(2,13,2)))

s = 0

for n in range(10):

   s += n

print(s)


#Primos

def es_primo(numero):

   resultado = True

   for divisor in range(2, numero):

       if (numero % divisor) == 0:

           resultado = False

           break

   return resultado


print(es_primo(13))

#----

def p1():
    s = 0
    for n in range(1, 10):

        if n % 7 == 0:

            break;

        s += n
        
        return s
    
print(p1())