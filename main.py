from flask import Flask

app=Flask(__name__)

@app.route("/hola")
def hola():
    return "hola mundo"



@app.route("/chau")
def goodbay():
    return "chau bro"


nombre = "tomasito"

@app.route("/sigma/", defaults={"nombre":None})
@app.route("/sigma/<nombre>")


def kkkkkk(nombre):
    return "hola " + nombre

@app.route("/sigma/<nombre>/<apellido>")
def rutanueva(nombre, apellido):
    return f"Hola {nombre} {apellido}"

app.run()