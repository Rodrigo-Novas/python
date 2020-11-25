import mysql.connector as mConnect
#aca lo que hago nps devuelve una instancia de bdd

mydbb=mConnect.connect(host='localhost',
     user='root',
     password='rodri7894561234r',
     database='prueba'
     )

#nos permite usar sentencias sql
cursor= mydbb.cursor()

#Ejecute versiones 
#cursor.execute("select * from usuario") #para select
#cursor.execute("show create table usuario") #te muestra el script con el que se creo la  tabla
#cursor.execute("update usuario set username='lautaro' where idUsuario= 1") #esto es para hacer el update
#el insert se hace de forma distinta asi que lo pongo en  insertar.py
output=cursor.execute("select * from usuario") 
#output=cursor.fetchone() este la diferencia que tiene con fetchall es que trae el primer fila sola
output= cursor.fetchall()
print(output)
# #cierro cursor y bdd (siempre primero la bdd y despues el cursor)
mydbb.close()
cursor.close()



