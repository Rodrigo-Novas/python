import mysql.connector as mCon
import click #se usa para crear tablas a traves de comandos en lugar de ingresar a mysql workbench y conectarnos
#g es una variable especial la vamos a usar para almacenar el usuario
from flask import current_app, g
from flask.cli import with_appcontext #con appcontext podemos acceder a las variables de nuestra aplicacion
from .schema import instructions

#funcion apra obtener bdd y cursor

def get_db():
    if "db" not in g:
        g.db=mCon.connect(
            host=current_app.config["DATABASE_HOST"],
            user=current_app.config["DATABASE_USER"],
            password=current_app.config["DATABASE_PASSWORD"],
            database=current_app.config["DATABASE"]
        )
        g.c= g.db.cursor()
    return g.db, g.c

def close_db(e=None):
    db= g.pop("db", None)#elimino el elemento db si su valor es none

    if db is not None: #si db no esta definido cierro conexion
        db.close()


def init_db():
    db,c=get_db()
    for i in instructions:
        c.execute(i)
    db.commit()


@click.command("init-db")#esto lo ejecuta desde la cmd
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Base de datos inicializada")


#de esta forma cuando termine de realiza la peticion cierra la conexion a nuestra bdd
def init_app(app):
    app.teardown_appcontext(close_db)#el metodo teardown lo que hara es ejecutar funciones como argumento cuando estemos terminando la ejecucion de algun endpoint
    app.cli.add_command(init_db_command)

#una vez colocado todo tengo que ir al cmd y poner:
# C:\Users\novasrodrigo\Desktop\Curso python\udemy\aplicacion web>set FLASK_DATABES_HOST='localhost'

# C:\Users\novasrodrigo\Desktop\Curso python\udemy\aplicacion web>set FLASK_DATABASE_HOST='localhost'

# C:\Users\novasrodrigo\Desktop\Curso python\udemy\aplicacion web>set FLASK_DATABASE_PASSWORD='rodri7894561234r'

# C:\Users\novasrodrigo\Desktop\Curso python\udemy\aplicacion web>set FLASK_DATABASE_
# FLASK_DATABASE_HOST='localhost'
# FLASK_DATABASE_PASSWORD='rodri7894561234r'

# C:\Users\novasrodrigo\Desktop\Curso python\udemy\aplicacion web>set FLASK_DATABASE_USER='rodrigoDev'

# C:\Users\novasrodrigo\Desktop\Curso python\udemy\aplicacion web>set FLASK_DATABASE='prueba'

# C:\Users\novasrodrigo\Desktop\Curso python\udemy\aplicacion web>flask init-db