from flask import Flask, render_template, request
from data import *
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", goals=goals, teachers_random=teachers_random, teachers=teachers)

@app.route('/all')
def all():
    return render_template("all.html", goals=goals, teachers=teachers)

@app.route('/goal/<goal_name>/')
def goal(goal_name):
    teachers_goal = []
    for teacher in teachers:
        if goal_name in teacher['goals']:
            teachers_goal.append(teacher)
    print(teachers_goal)
    return render_template("goal.html", goals=goals, teachers_goal=teachers_goal, goal_name=goal_name)


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


@app.route('/booking/<int:teacher_id>/<day>/<time>')
def booking(teacher_id, day, time):
    return render_template("booking.html", teachers=teachers, teacher_id=teacher_id, weekdays=weekdays, day=day, time=time)


@app.route('/booking_done', methods=['POST'])
def booking_done():
    clientweekday = request.form.get("clientWeekday")
    clienttime = request.form.get("clientTime")
    clientteacher = request.form.get("clientTeacher")
    clientname = request.form.get("clientName")
    clientphone = request.form.get("clientPhone")
    print(clientweekday, clienttime, clientteacher, clientphone, clientname)
    return render_template("booking_done.html", clienttime=clienttime, clientteacher=clientteacher, clientweekday=clientweekday, clientname=clientname, clientphone=clientphone)

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


teachers_random = random.sample(teachers, 6)



if __name__ == '__main__':
    app.run()