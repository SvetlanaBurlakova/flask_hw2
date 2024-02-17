"""
Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества словв тексте и переход на страницу
с результатом.
"""
from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        length = len(text.split())
        return render_template('count_words.html', length=length)
    return render_template('base.html')



if __name__ == '__main__':
    app.run()
