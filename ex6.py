"""
Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""
from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if int(age) >= 18:
            return render_template('age_correct.html', name=name, age=age)
        else:
            return render_template('age_noncorrect.html', name=name, age=age)
    return render_template('base_6.html')


if __name__ == '__main__':
    app.run()