import mysql.connector as mConnector


myBdd=mConnector.connect(host="localhost", user="root", password="rodri7894561234r", database="prueba")

cursor=myBdd.cursor()

cursor.execute("delete from Usuario where idUsuario=3")
cursor.execute("select * from Usuario")
output=cursor.fetchall()
print(output)


myBdd.commit()

cursor.close()
myBdd.close()