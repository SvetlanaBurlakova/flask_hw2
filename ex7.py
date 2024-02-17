"""
Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
При нажатии на кнопку будет произведено перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num = request.form.get('number')
        square = float(num)**2
        return render_template('num_and_square.html', num=num, square=square)
    return render_template('base_7.html')



if __name__ == '__main__':
    app.run()