from flask import Flask, render_template, abort
from data import *
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", goals=goals, teachers_number=teachers_number, teachers=teachers)

@app.route('/all')
def all():
    return render_template("all.html", goals=goals, teachers=teachers)

@app.route('/goals/<goal>')
def all_goals(goal):
    return render_template("goal.html")


@app.route('/profile/<int:uin>')
def profile(uin):
    work_week = {}
    days_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    num = 0
    for i in range(1):
        for day in teachers[uin]['free']:
            days_new = {x: True for x in teachers[uin]['free'][day].keys() if teachers[uin]['free'][day][x] == True}
            work_week[days_week[num]] = days_new
            num += 1
    return render_template("profile.html", teachers=teachers, uin=uin, teachers_number=[1], goals=goals, weekdays=weekdays, work_week=work_week)


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



if __name__ == '__main__':
    app.run()