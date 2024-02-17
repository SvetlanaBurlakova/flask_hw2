"""
Создать страницу, на которой будет форма для ввода имени и электронной почты
При отправке которой будет создан cookie файл с данными пользователя
Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""
from flask import Flask, render_template, request, make_response, redirect, url_for, session

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('greetings')))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response
    return render_template('base_9.html')


@app.route('/greetings', methods=['POST', 'GET'])
def greetings():
    name = request.cookies.get('name')
    if request.method == 'POST':
        request.set_cookie = None
        return render_template('base_9.html')
    return render_template('greeting_and_quit.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)