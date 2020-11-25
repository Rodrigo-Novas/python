import mysql.connector as mConnect


myBdd= mConnect.connect(host="localhost", user="root", password="rodri7894561234r", database="prueba")

cursor=myBdd.cursor()

cursor.execute("update Usuario set username='josema' where idUsuario=1")

cursor.execute("select * from Usuario")
output = cursor.fetchall() #para mostrar todo
print(output)

myBdd.commit()

cursor.close()
myBdd.close()