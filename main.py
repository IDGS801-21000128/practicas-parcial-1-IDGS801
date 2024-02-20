from flask import Flask, render_template, request
import forms
import coloresForms
import math
from io import open


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


color_converter = coloresForms.ColorConverter()

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

        color1 = color_converter.get_color(b1, 1)
        color2 = color_converter.get_color(b2, 1)
        color3 = color_converter.get_color(str(b3), 2)
        tolerancia = 'Oro' if tol == 0.05 else 'Plata'

        color_eng1 = color_converter.get_english_color(color1)
        color_eng2 = color_converter.get_english_color(color2)
        color_eng3 = color_converter.get_english_color(color3)
        tol_eng = '#BEB23F' if tolerancia == "Oro" else "#BABAB3"

        valor = int(b1 + b2) * b3
        valorMaximo = (valor * tol) + valor
        valorMinimo =  valor - (valor * tol)
        return render_template("colores_resistencia.html", valor=valor, valorMaximo=valorMaximo, valorMinimo=valorMinimo,color1=color1, 
                               color2=color2, 
                               color3=color3, tolerancia=tolerancia, color_eng1=color_eng1, color_eng2=color_eng2, color_eng3=color_eng3,
                               tol_eng=tol_eng)
    return render_template("colores_resistencia.html")


#-----------------------Parcial 2 traduccion

@app.route("/traduccion", methods=['GET','POST'])
def guardarTraduccion():
    campos = forms.fieldsTraduccion(request.form)
    campos2 = forms.searchTraduction(request.form)
    ingles = ''
    espanol = ''
    result = ''
    if request.method=='POST':
        if "ingles" in request.form and "espanol" in request.form and campos.validate():
            ingles = campos.ingles.data
            espanol = campos.espanol.data
            print(ingles)
            archivo1 = open('archivo.txt', 'a')
            archivo1.write(f"{ingles}:{espanol}\n")
            archivo1.close()   
        elif "busqueda" in request.form  and campos2.validate():
            idioma = campos2.idioma.data
            print(idioma)
            busqueda = campos2.busqueda.data
            with open("archivo.txt", "r") as file:
                translations = [line.strip().split(":") for line in file]

            translation = None
            for pair in translations:
                if pair[0] == busqueda and idioma == 'Ingles':
                    translation = pair[1]
                    result = translation
                    break
                elif pair[1] == busqueda and idioma == 'Español':
                    translation = pair[0]
                    result = translation
                    break

            if translation == None:
                translation="Translation not found"

    #if request.method=='POST' and campos.validate() and request.form["search"]:
     #   idioma = campos.idioma.data
      #  busqueda = campos.busqueda.data
      #  archivo1 = open('archivo.txt', 'a')
       # print()
        
    return render_template("traduccion.html", form=campos, ingles = ingles, espanol = espanol, form2=campos2, result = result)



if __name__ == "__main__":
    app.run(debug=True)