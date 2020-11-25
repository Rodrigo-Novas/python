import os #nos permite acceder a ciertar cosas del sistema operativo
from flask import Flask


def create_app(): #funcion para testing o crear varias instancias de la app
    app= Flask(__name__)
    #NOS PERMITE VER LOS DATOS DEL USUARIO, PARA SABER QUIEN NAVEGA EN NUESTRA APP
    app.config.from_mapping(
        SECRET_KEY= "mikey",#ESTE STRING NOS SIRVE PARA FLASK, debemos cambiar esto por un string mas complejo para que los hackers no lo puedan descifrar
        DATABASE_HOST=os.environ.get("FLASK_DATABASE_HOST"),
        DATABASE_PASSWORD=os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER=os.environ.get("FLASK_DATABASE_USER"),
        DATABASE=os.environ.get("FLASK_DATABASE")
        )
    
        
    @app.route("/hola")
    def hola():
        return "hola mundo"
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register.blueprint(auth.bp)#llamo al blueprint
    
    
    return app #siempre retornar app
    