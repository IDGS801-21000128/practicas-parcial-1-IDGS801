from flask import Flask, render_template, request
import forms
import coloresForms
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

#Examen -----------------------------------------------

color_map1 = {
    '0': 'Negro',
    '1': 'Cafe',
    '2': 'Rojo',
    '3': 'Naranja',
    '4': 'Amarillo',
    '5': 'Verde',
    '6': 'Azul',
    '7': 'Violeta',
    '8': 'Gris',
    '9': 'Blanco'
}

color_map2 = {
    '1': 'Negro',
    '10': 'Cafe',
    '100': 'Rojo',
    '1000': 'Naranja',
    '10000': 'Amarillo',
    '100000': 'Verde',
    '1000000': 'Azul',
    '10000000': 'Violeta',
    '100000000': 'Gris',
    '1000000000': 'Blanco'
}
color_english = {
     'Negro': 'Black',
     'Cafe': 'Brown',
     'Rojo': 'Red',
     'Naranja': 'Orange',
     'Amarillo': 'Yellow',
     'Verde': 'Green',
     'Azul': 'Blue',
     'Violeta': 'Violet',
     'Gris': 'Gray',
     'Blanco': 'White'
}


@app.route("/resistencia", methods=['GET','POST'])
def calcularResistencia():
    campos = coloresForms.coloresForms(request.form)
    valor = 0.0
    valorMaximo = 0.0
    valorMinimo = 0.0
    if request.method == "POST":
        b1 = campos.b1.data
        b2 = campos.b2.data
        b3 = int(campos.b3.data)
        tol = float(campos.tol.data)

        color1 = color_map1.get(b1, 'Desconocido')
        color2 = color_map1.get(b2, 'Desconocido')
        color3 = color_map2.get(str(b3), 'Desconocido')
        tolerancia = 'Oro' if tol == 0.05 else 'Plata'

        color_eng1 = color_english.get(color1, "Desconocido")
        color_eng2 = color_english.get(color2, "Desconocido")
        color_eng3 = color_english.get(color3, "Desconocido")
        tol_eng = '#BEB23F' if tolerancia == "Oro" else "#BABAB3"

        valor = int(b1 + b2) * b3
        valorMaximo = (valor * tol) + valor
        valorMinimo =  valor - (valor * tol)
        return render_template("colores_resistencia.html", valor=valor, valorMaximo=valorMaximo, valorMinimo=valorMinimo,color1=color1, 
                               color2=color2, 
                               color3=color3, tolerancia=tolerancia, color_eng1=color_eng1, color_eng2=color_eng2, color_eng3=color_eng3,
                               tol_eng=tol_eng)
    return render_template("colores_resistencia.html")



if __name__ == "__main__":
    app.run(debug=True)