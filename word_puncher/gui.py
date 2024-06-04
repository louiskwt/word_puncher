from http.server import HTTPServer, SimpleHTTPRequestHandler
import cgi

# TODO: learn to roll a small local server for the gui
class HttpHandler(SimpleHTTPRequestHandler):
    #Override the default do_POST method
    def log_message(self, format, *args):
        pass 

    def do_GET(self):
        if self.path == '/':
            self.path = 'gui.html'
        return SimpleHTTPRequestHandler.do_GET(self)


    def cgiFieldStorageToDict(self, fieldStorage):
        """ Get a plain dictionary rather than the '.value' system used by the
           cgi module's native fieldStorage class. """
        pass

    def do_POST(self):
        path = self.path
        action = {
                '/ajax/upload-file': '',
                '/ajax/upload-ans': '',
                '/ajax/generate-exercise': '',
                '/ajax/download': '',
                }.get(path)
        if not action:
            return
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
             'CONTENT_TYPE':self.headers['Content-Type'],
            })
        res = action(form)
        self.send_response(200)

def run_gui(port):
    httpd = HTTPServer(('localhost', port), HttpHandler)
    print(f"Running Word Puncher on localhost port: {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_gui(8000)