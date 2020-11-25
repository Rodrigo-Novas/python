diccionario={"nombre":"rodrigo",
             "apellido":"novas",
             "edad":34}
print(diccionario["nombre"])
print(diccionario.get("nombre"))#lo mismo que diccionario["nombre"]
diccionario.get("nombre") ="JOSE" #MODIFICO EL VALOR QUE CONTIENE NOMBRE
print(diccionario.values())#me trae todos los valores
print(diccionario.items())#me trae el valor y key de todos como una lista que contiene una tupla
listaNombres=["juan","ernesto","rodrigo", "miguel"]
listaApellidos=["rodrguez","sabato","rodrigo", "miguel"]
listaEdad=[22,3,55, 40]
diccionarioLista={"nombre": listaNombres, "apellido": listaApellidos, "edad": listaEdad} #creo diccionario con listas
print(diccionarioLista)

#diccionarios anidados

diccionarioAnidado={
    "Felinos"{
        "tipo": "Gato",
        "edad": 34
    },
    "Serpientes":
        {
            "tipo": "Mamba Negra"
            "edad": 12
        }
}

#tambien se puede crear un diccionario usando dict
perros= dict(nombre:"jorge", edad=34)
print(perros)

