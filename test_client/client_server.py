from bottle import route, post, run, template, request
from text_file_parser import TextFileParser

@route("/")
def index():
    return template('client', output='')

@post('/upload-file')
def upload_file():
    file = request.forms.get('text-file')
    if file:
        print("here", request.forms.get('text-file'))
        parser = TextFileParser(file)
        parser.detect_file_type()
        data = parser.parse()
        print(data)
        output_data = ['<div>' + line + '</div>' for line in data]
        return template('client', output=''.join(output_data))
    else:
        return template('client', output="File output here")

run(host='localhost', port=8000, debug=True, reloader=True)