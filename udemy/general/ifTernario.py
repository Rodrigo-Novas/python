print("Cuando es true") if 2<5 else print("Cuando es false") #ternario
#listcomprehension
lista=["hola", "niñes"]
listComprehension=[n for n in range(len(lista))]
listComprehension2=[i.join(i ' ') for i in lista]
#lambda
anonima= lambda n : n+2

print(listComprehension)
print(anonima(4))
print(listComprehension2)