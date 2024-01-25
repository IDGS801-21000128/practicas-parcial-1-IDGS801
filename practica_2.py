from flask import Flask, render_template, request

app=Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)