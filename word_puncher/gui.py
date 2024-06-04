from http.server import HTTPServer, SimpleHTTPRequestHandler
from utils import generate_exercise_with_answer_keys
import cgi
import re

class GUI:
    '''
        the main logic for the web based gui
        it acts like a controllers
    '''
    def __init__(self):
        self.selected_words = []
        self.selected_text = []

    def parse_uploaded_file(self, data):
        print(data)
        # if is_word:
        #     pattern = r'>(.*?)<'
        #     text = [s for s in re.findall(pattern, text_data) if s and s!='\r']
        # else:
        #     text = [line.rstrip('\n') for line in text_data if line.rstrip('\n')]

        # self.selected_text = text
        # return [[word for word in line] for line in text] 

    def parse_selected_words(self, text_data):
        self.selected_words = text_data
    
    def generate_exercise(self):
        return generate_exercise_with_answer_keys(self.selected_text, self.selected_words)


# TODO: learn to roll a small local server for the gui
class HttpHandler(SimpleHTTPRequestHandler):
    #Override the default do_POST method
    def log_message(self, format, *args):
        pass 

    def do_GET(self):
        if self.path == '/':
            self.path = 'gui.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        path = self.path
        action = {
                '/upload-file': gui.parse_uploaded_file,
                '/ajax/upload-ans': gui.parse_selected_words,
                '/ajax/generate-exercise': gui.generate_exercise,
                '/ajax/download': '',
                }.get(path)
        if not action:
            return
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
             'CONTENT_TYPE':self.headers['Content-Type'],
             'CONTENT_LENGHTH': self.headers['Content-Length']
            })
        print(form.getvalue("file"))
        form_data = self.cgiFieldStorageToDict(form)
        res = action(form_data)
        print(res)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b'File uploaded successfully!')

def run_gui(port):
    global gui
    gui = GUI()
    httpd = HTTPServer(('localhost', port), HttpHandler)
    try:
        httpd.handle_request()
        httpd.serve_forever()
        print(f"Running Word Puncher on localhost port: {port}...")
    except KeyboardInterrupt:
        print("shutting down")
        httpd.socket.close()


if __name__ == "__main__":
    run_gui(8000)