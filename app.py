# Put your app here
from flask import Flask
from flask import request
import operations
app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.add(a, b)
    return str(result)
   

@app.route("/sub")
def sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.sub(a, b)
    return str(result)
    
   
@app.route("/mult")
def mult():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    result = operations.mult(a, b)
    return str(result)

@app.route("/div")
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    result = operations.div(a, b)
    return str(result)
