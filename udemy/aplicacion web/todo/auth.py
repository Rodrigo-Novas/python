import functools #funciones utiles
from flask import(
    Blueprint, flash, g,render_template, request,url_for, session
)#flash nos permite enviar mensajes genericos a nuestras plantillas
from werkzeug.security import check_password_hash, generate_password_hash #el primero lo que hace es ver si la contraseña nueva es igual a la otra y el otro crea un hash para la password
from todo.db import get_db


#el blue print es mas que nada un conjunto de modulos que hacen sentido
bp= Blueprint("auth", __name__, url_prefix=="/auth")#lo que hace url prifix es darle un prefijo a todas las urls



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="POST":
        username=request.form("username")
        password=request.form["password"]
        db,c=get_db
        error= None
        c.execute(
            "select id from user where username = %s"
        )
        if not username:
            error="username es requerido"
        if not password:
            error= "password es requerido"
        elif c.fetchone() is not None:
            error= f"usuario {username} se encuentra registrado"
        
        
        if error is None:
            c.execute(
                "insert into user (username,password) values (%s, %s)",
                 (username, generate_password_hash(password)) #genera validacion de password
            )
            db.commit()
            
            return redirect(url_for("auth.login")) #redirecionamos a auth.login
        
        flash(error)
    
    return render_template("auth/register.html")


@bp.route("/login", methods=["GET", "POST"])
def loguin():
    if request.method=="POST":
        username = request.form["username"]
        password =request.form["password"]
        db, c = get_db()
        error = None
        c.execute(
            
            "select * from user where username = %s", (username,)
        )
        
        if user is None: #esto es por si el hacker intenta ingresa un usuario que noe existe
            error = "usuario y o contraseña invalida"
        elif not check_password_hash(user["password"], password): #si el chequeo no es el mismo entonces debemos enviar otro mensaje de error    
            error = "Usuario y/o contraseña invalida"
            
        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))
        
        flash(error)
        
        
        return render_template("auth/login.html")
    
