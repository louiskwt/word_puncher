from bottle import route, run, template

@route("/")
def index():
    return template('client')

run(host='localhost', port=8000, debug=True, reloader=True)