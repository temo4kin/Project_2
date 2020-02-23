from flask import Flask, render_template, abort
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/goals/<goal>')
def goals(goal):
    return render_template("goal.html")


@app.route('/profiles/<uin>')
def profiles(uin):
    return render_template("profile.html")


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


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", 404


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500

'''
@app.errorhandler(404)
def not_found(e):
    output = render_template("404.html", title=title, subtitle=subtitle, departures=departures, description=)
    return output
'''

with open('data.json', 'r') as f:
    team = json.loads(f.read())

print(team)

if __name__ == '__main__':
    app.run()