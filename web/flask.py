from flask import Flask, render_template,request
import subprocess,re

from core import actions
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/additionPage", methods = ['POST'])
def addition_page():
    nb1= request.form['nb1']
    nb2= request.form['nb2']
    if not nb1:
        error="Number1 is not declared. Please enter the first number."
        return render_template("home.html",error=error)
    if not nb2:
        error="Number2 is not declared. Please enter the second number."
        return render_template("home.html",error=error)
    if not nb1.isdigit():
        error="Number1 is not a number. Please re-enter the first number."
        return render_template("home.html",error=error)
    if not nb2.isdigit():
        error="Number2 is not a number. Please re-enter the second number."
        return render_template("home.html",error=error)
    result = actions.do_addition(nb1,nb2)
    return render_template("result.html",nb1=nb1,nb2=nb2,result=result)

@app.route("/greetPage", methods = ['POST'])
def greet_page():
    name=request.form['name']
    pokemon=request.form['pokemon']
    b_pokemon=True
    if pokemon != "True":
        b_pokemon=False
    if not name:
        error="Name is not declared. Please enter a name."
        return render_template("home.html",error=error)
    result = actions.say_hello(name,b_pokemon)
    return render_template("result.html",name=name,result=result)

if __name__ == "__main__":
    app.run(debug=True)