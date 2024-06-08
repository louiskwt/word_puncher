from bottle import route, post, run, template

@route("/")
def index():
    return template('client', output='')

@post('/upload-file')
def upload_file():
    return template('client', output="File output here")

run(host='localhost', port=8000, debug=True, reloader=True)