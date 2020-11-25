from flask import Flask, render_template


#Nos permite crear nuestras urls 
app = Flask(__name__) #esto crea un servidor


#Para crear una ruta usamos un decorador @
@app.route("/") 
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
#una aplicacion web siempre debe estar escuchando las peticiones de los navegadores
if __name__ == "__main__":
    app.run(debug=True) #Poner el debug=true lo que hace es que el servidor entra en modo debug y asi me ahorro tener que colocar a cada rato ctrl+c