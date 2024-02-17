"""
Создать страницу, на которой будет форма для ввода двух чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с
результатом.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number1 = request.form.get('number1')
        number2 = request.form.get('number2')
        oper = request.form.get('operations')
        if oper == 'add':
            result = float(number1) + float(number2)
        elif oper == 'sub':
            result = float(number1) - float(number2)
        elif oper == 'mult':
            result = float(number1) * float(number2)
        else:
            result = float(number1) / float(number2)
        return render_template('math_calculations.html', result=result)
    return render_template('base_5.html')



if __name__ == '__main__':
    app.run()