from flask import render_template, request
from app import app

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']
    if operation == 'add':
        result = float(num1) + float(num2)
        return render_template('index.html', result=result, title='Home')
    elif operation == 'subtract':
        result = float(num1) - float(num2)
        return render_template('index.html', result=result, title='Home')
    elif operation == 'multiply':
        result = float(num1) * float(num2)
        return render_template('index.html', result=result, title='Home')
    elif operation == 'divide':
        result = float(num1) / float(num2)
        return render_template('index.html', result=result, title='Home')
    else:
        return render_template('index.html', title='Home')
