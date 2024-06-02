import http.server
import cgi

# TODO: learn to roll a small local server for the gui
class HttpHandler(http.server.SimpleHTTPRequestHandler):
    #Override the default do_POST method
    def log_message(self, format, *args):
        pass 

    def cgiFieldStorageToDict(self, fieldStorage):
        """ Get a plain dictionary rather than the '.value' system used by the
           cgi module's native fieldStorage class. """
        params = {}
        for key in fieldStorage.keys():
            params[key] = fieldStorage[key].value
        return params

    def do_POST(self):
        pass