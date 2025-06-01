from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("calculator.html")


@app.route("/result", methods=["POST"])
def result():
    expression = request.form["expression"]
    operators = ["+", "-", "*", "/"]

    for op in operators:
        if op in expression:
            exp = expression.split(op)
            if exp[0].isdigit() and exp[1].isdigit():
                num1 = float(exp[0])
                num2 = float(exp[1])
                if (op == '+'):
                    res = num1 + num2
                elif (op == '-'):
                    res = num1 - num2
                elif (op == '*'):
                    res = num1 * num2
                elif (op == '/'):
                    res = num1 / num2
                with open("history.csv","a")as f: 
                    lines=f"{exp[0]},{op},{exp[1]},=,{res}\n" 
                    f.write(lines) 
                return render_template("calculator.html", res=res)
            else:
                return "<h1>Invalid Expression</h1>"

    return "<h1>Wrong input</h1>"
@app.route("/history", methods=["GET"])
def history():
    with open("history.csv","r")as f:
        history=f.readlines()
        return render_template("calculator.html",history=history)

if __name__ == "__main__":
    app.run(debug=True)
