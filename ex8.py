"""
Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением,
где будет выведено "Привет, {имя}!".

"""
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            flash(f'Привет, {name}')
            return render_template('greeting.html')
    return render_template('base_8.html')



if __name__ == '__main__':
    app.run()