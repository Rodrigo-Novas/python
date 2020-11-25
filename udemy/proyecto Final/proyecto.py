from flask import Flask, render_template, request, url_for, redirect
import mysql.connector as mCon

#conexion a la bdd

conn= mCon.connect(host="localhost", user="root", password="rodri7894561234r", database="prueba")

#cursor

cursor= conn.cursor(dictionary=True) #por defecto esto retorna una tupla si le coloco dictionary=true retorna un diccionario








#para correrlo debo ir a el cmd y colocar lo siguiente

# C:\Users\novasrodrigo>set FLASK_APP=proyecto.py

# C:\Users\novasrodrigo>flask run
#Poner el debug=true lo que hace es que el servidor entra en modo debug y 
# asi me ahorro tener que colocar a cada rato ctrl+c
#set FLASK_ENV=development se coloca de esta forma el modo debug

#esto es para tener el nombre
app= Flask(__name__)

#uso un decorador en app
@app.route("/")#el codigo que se va a ejecutar despues se va a ejecutar en la raiz
def index():
    return "hola mundo"

#colocando int lo que hago es forzar a la ruta que tome si o si un dato entero sino larga una excepcion
@app.route("/info/<int:post_id>") #con el <usuario> lo quehago es pasarle un valor por la ruta y que se vea reflejado en la funcion
def info(post_id):
    return "El id del post es: " + post_id


#Nosotro podemos configurar las rutas para que sean accesibles a traves de los metodos
#un metodo web nos indica la accion deseada sobre el sitio que construimos (get, post, delete)
#get listar, post publicat, put actualizar y delete eliminar
#COLOCAR ESTA SENTENCIA EN EL CMD curl -noproxy POST http://127.0.0.1:5000/info2/1 nos sirve para probar algun endpoint
#EN DONDE VA POST DEL PASO ANTERIOR PUEDE IR CUALQUIER COSA
@app.route("/info2/<post_id>", methods=['GET']) #LE INDICO QUE PUEDO ACCEDER A ESTA RUTA MEDIANTE ESOS METODOS
def getinfo2(post_id):
    if request.method=='GET':
        return "El id del post es: " + post_id
    else:
        return "Esto no es un metodo GET"

@app.route("/info2/<post_id>", methods=['POST']) #LE INDICO QUE PUEDO ACCEDER A ESTA RUTA MEDIANTE ESOS METODOS
def postinfo2(post_id):
    if request.method=='POST':
        return "El id del post es: " + post_id
    else:
        return "Esto no es un metodo POST"


#dentro de el cmd colocamos curl -noproxy -d "llave1=dato1&llave2=dato2" -X POST http://localhost:5000/lele

@app.route("/aboutus", methods=['POST', 'GET'])
def aboutus():
    #abort(403) esto lanza un error web aborta la peticion, detiene la ejecucion y devuelve un codigo
    #return redirect(url_for('postinfo2', post_id=2)) #redirecciona a otra pagina, SIEMPRE DEBO USAR RETURN SI NO LO PONGO MUERO 
    #print(url_for('postinfo2', post_id=2)) #Imprume el contenido de la otra pagina usando esto, tengo que nombrar el metodo de la funcion. El segundo atributo de la funcion es por si tiene algun atributo variable el route
    # print(request.form)
    # print(request.form["llave1"]) #con esto le envio la informacionr requerida por el metodo
    # print(request.form["llave2"])
    cursor.execute("select* from Usuario")
    usuarios= cursor.fetchall()
    return render_template("aboutus.html", usuarios=usuarios) #esto te redirecciona a un html, usa como template ese html para la ruta especificada

@app.route("/pruebaJson/<nombre>", methods=["POST", "GET"])
def pruebaJson(nombre):
    return{"username":nombre,
            "emal": "chanchito@feliz.com"}

#--------------

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", mensaje="hola mundo")


@app.route("/crear", methods=["POST", "GET"])
def crear():
    if request.method=="POST":
        username= request.form['username']
        email= request.form['email']
        edad= request.form['edad']
        sql ="insert into Usuario(username, email, edad) values(%s,%s,%s)"
        values=(username, email,edad)
        cursor.execute(sql, values)
        conn.commit()
        return redirect(url_for("aboutus"))
    return render_template("crear.html")