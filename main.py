from flask import Flask, render_template, request
import forms
import math


app=Flask(__name__)

#Practica 2 ----------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/resultado', methods=['POST'])
def resultado():
    n1 = float(request.form['n1'])
    n2 = float(request.form['n2'])
    operation = request.form['operation']

    result = None

    if operation == '+':
        result = n1 + n2
        return "La suma de {} + {} = {}".format(n1,n2, result)
        
    elif operation == '-':
        result = n1 - n2
        return "La resta de {} + {} = {}".format(n1,n2, result)
    elif operation == '*':
        result = n1 * n2
        return "La multiplicacion de {} + {} = {}".format(n1,n2, result)
    elif operation == '/':
        if n2 != 0:
            result = n1 / n2
            return "La division de {} + {} = {}".format(n1,n2, result)
        else:
            return "Error: Division Indeterminada"     


#Practica 3 ------------------------------------------
@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    campos = forms.filedsForm(request.form)
    x1 = ""
    y1 = ""
    x2 = ""
    y2 = ""
    resultado = None
    if request.method=='POST':
        x1 = campos.x1.data
        y1 = campos.y1.data
        x2 = campos.x2.data
        y2 = campos.y2.data
        resultado = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
    return render_template("distancia_dos_puntos.html", form=campos, x1=x1, y1=y1, x2=x2, y2=y2, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)