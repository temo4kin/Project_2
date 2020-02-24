from flask import Flask, render_template, abort
from data import *
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", goals=goals, teachers_number=teachers_number, teachers=teachers)

@app.route('/goals/<goal>')
def all_goals(goal):
    return render_template("goal.html")


@app.route('/profile/<int:uin>')
def profile(uin):
    return render_template("profile.html", teachers=teachers, uin=uin, teachers_number=[1])


@app.route('/request')
def request():
    return render_template("request.html")


@app.route('/request_done')
def request_done():
    return render_template("request_done.html")


@app.route('/booking')
def booking():
    return render_template("booking.html")


@app.route('/booking_done')
def booking_done():
    return render_template("booking_done.html")

'''
@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", 404


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500
'''

@app.errorhandler(500)
def render_server_error(error):
    return render_template("500.html", goals=goals), 500


@app.errorhandler(404)
def render_not_found(error):
    return render_template("404.html", goals=goals), 404


teachers_number = []

while len(teachers_number) != 6:
    a = random.randint(0, 11)
    if a in teachers_number:
        a = random.randint(1, 16)
    else:
        teachers_number.append(a)

print(teachers_number)

print(teachers[0]['name'])

if __name__ == '__main__':
    app.run()