from flask import Flask, redirect, url_for, render_template, request, jsonify, app
import pandas as pd
import json
app = Flask(__name__)

class Calculations(object):

    def __init__(self):
        pass

    def sum(self):
        # http://127.0.0.1:5000/sum?number1=2&number2=2
        number1 = request.args['number1']
        Number1 = float(number1)
        number2 = request.args['number2']
        Number2 = float(number2)
        result = str(Number1 + Number2)
        return number1 + " + " + number2 + " = " + (result)

    def grade(self):
        # http://127.0.0.1:5000/calculate_exam_grade

        if request.method == 'POST':
            spoints = request.form['number']
            fpoints = float(spoints)
            if (fpoints >= 0 and fpoints <= 49):
                grade = 5
                return "Your grade is:" + str(grade)

            elif (fpoints > 49 and fpoints <= 59):
                grade = 6
                return "Your grade is:" + str(grade)

            elif (fpoints > 59 and fpoints <= 69):
                grade = 7
                return "Your grade is:" + str(grade)

            elif (fpoints > 69 and fpoints <= 79):
                grade = 8
                return "Your grade is:" + str(grade)

            elif (fpoints > 79 and fpoints <= 89):
                grade = 9
                return "Your grade is:" + str(grade)

            elif (fpoints > 89 and fpoints <= 100):
                grade = 10
                return "Your grade is:" + str(grade)

            else:
                return "Exam points are out of range!"

        return render_template("calculate_exam_grade.html")

    def minmax(self):
        # http://127.0.0.1:5000/minmax
        array = '{"values": [0,3,4,18,333]}'
        data = json.loads(array)

        if (len(data['values']) > 1):
            minimum = min(data['values'])
            maximum = max(data['values'])
            return "Minimum value:" + str(minimum) + " , maximum value:" + str(maximum)

        elif (len(data['values']) == 0):
            return "The list is empty!"

        else:
            return "Minimum and maximum value is: " + str(data['values'])
