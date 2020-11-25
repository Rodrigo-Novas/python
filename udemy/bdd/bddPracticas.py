#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
 
import sqlite3
 
while True:
    
    print("""
    Administración de base de datos 'productos.db'
    *--------------------------------------------*
        Menu de opciones:
        1) Agregar un nuevo registro
        2) Consultar registros
        3) Borrar registros
        4) Salir
    *--------------------------------------------*
    """)
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        while True:
            try:
                ID = int(input("Ingrese un ID: "))
                break
            except ValueError:
                print("Error de tipo de dato: ID debe ser nro. entero")
        while True:
            nombre = input("Ingrese el nombre del producto: ")
            if len(nombre) > 0 and nombre[0] !=" ":
                break
            else:
                print("No se ingresó un nombre o su primer caracter es vacío")
        while True:
            try:
                precio = int(input("Ingrese un precio: "))
                break
            except ValueError:
                print("Error de tipo de dato: ID debe ser nro. entero")
        
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos VALUES (?,?,?)",(ID, nombre, precio))
        conn.commit()
        conn.close()
        print("Se ha guardado el registro")
        
    elif opcion == "2":
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        for dato in datos:
            print(dato)
        conn.close()
    
    elif opcion =="3":
        while True:
            try:
                registro = int(input("Ingrese el ID del producto a eliminar: "))
                break
            except ValueError:
                print("Error de tipo de dato: ID debe ser nro. entero")
        
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = {}".format(registro))
        conn.commit()
        conn.close()
        print("Registro eliminado")
        
    elif opcion == "4":
        print("Hasta luego...")
        break
    
    else:
        print("Opción incorrecta")