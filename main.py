from flask import Flask, redirect, url_for, render_template, request, jsonify, app
import json
from Calculations import Calculations

app = Flask(__name__)

Calculations=Calculations()
@app.route("/hello")
def hello():
    #http://127.0.0.1:5000/hello?name=<name>
    name = request.args['name']

    if all(char.isalpha() for char in name):
        return "Hello " + name
    return "Only Letters Please!"

@app.route("/sum")
def sum():
    # http://127.0.0.1:5000/sum?number1=2&number2=2
   return Calculations.sum()

@app.route("/calculate_exam_grade",methods = ['POST', 'GET'])
def grade():
    # http://127.0.0.1:5000/calculate_exam_grade
    return Calculations.grade()

@app.route("/minmax")
def minmax():
    # http://127.0.0.1:5000/minmax
    return Calculations.minmax()

if __name__=='__main__':
    app.run(debug=True)