from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/goals/<goal>')
def departure(goal):
    return render_template("goal.html")


@app.route('/profiles/<uin>')
def tour(uin):
    return render_template("profile.html")

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
if __name__ == '__main__':
    app.run()