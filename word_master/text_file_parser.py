# Parser for files

class TextFileParser:
    def __init__(self, path):
        self.path = path
    
    def parse_file(self):
        with open(self.path) as file:
            return [line.rstrip('\n') for line in file]

