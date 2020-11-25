import mysql.connector as mConnect


mybdd=mConnect.connect(host="localhost", user="root", password="rodri7894561234r", database="prueba")

cursor= mybdd.cursor()

#cursor.execute("show create table Usuario")

#coloco dos variables una tupla y un string que va a ser la sentencia
values=("roberto", "bolaños", 33)
sentencia="insert into Usuario (username, email, edad) values(%s,%s,%d)"

#ejecuto sentencia
mybdd.execute(sentencia, values)

#para que se vean los datos en la bdd debo hacer un commit
#esto debe hacerse para todos las sentencias que impliquen tener que modificar la tabla o crearla
cursor.commit()


#cierro las conexiones
cursor.Close()
cursor.Close()