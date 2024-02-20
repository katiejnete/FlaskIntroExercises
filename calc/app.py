# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/<op>')
def do_math(op):
    """Handles GET requests like /<operation>?a=num&b=num"""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    if op == 'add':
        result = add(a,b)
    elif op == 'sub':
        result = sub(a,b)
    elif op == 'mult':
        result = mult(a,b)
    elif op == 'div':
        result = div(a,b)
    return f"Result is {result}."

OPS = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

@app.route('/math/<op>')
def all_math(op):
    """Handles GET request as a single view function."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"Result is {OPS[op](a,b)}."