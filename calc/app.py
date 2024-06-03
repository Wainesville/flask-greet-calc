# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add():
    "Add a and b parameters"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results =str( a + b)
    
    return results

@app.route('/sub')
def sub():
    "Subtract a and b parameters"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results =str( a - b)
    
    return results

@app.route('/mult')
def mult():
    "Multiplys a and b parameters"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results =str( a * b)
    
    return results

@app.route('/div')
def div():
    "Div a and b parameters"

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    results =str( a / b)
    
    return results

operator = {
    "add" : add,
    "sub" : sub,
    "mult": mult,
    "div" : div,
}

@app.route("/calculator/<operation>")
def calculator(operation):

    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    results = operator[operation](a,b)

    return str(results)