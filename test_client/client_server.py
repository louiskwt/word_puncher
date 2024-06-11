from bottle import route, post, run, template, request, static_file
from text_file_parser import TextFileParser
from utils import strip_punctuations, find_punctuation

@route("/")
def index():
    return template('client', output='')

@post('/upload-file')
def upload_file():
    file = request.forms.get('text-file')
    if file:
        parser = TextFileParser(file)
        parser.detect_file_type()
        data = parser.parse()
        output_data, id_count = [], 0
        for line in data:
            words = line.split(" ") 
            processed_words = []
            for word in words:
                punctuations, cleaned_word = find_punctuation(word), strip_punctuations(word)
                processed_words.append('<span id="' + str(id_count) + '">' + punctuations['front'] + cleaned_word + punctuations['end'] + '</span>')
                id_count += 1

            output_data.append("<div>" +  " ".join(processed_words) + "</div>")
        return template('client', output=''.join(output_data))
    else:
        return template('client', output="File output here")
    

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

run(host='localhost', port=8000, debug=True, reloader=True)