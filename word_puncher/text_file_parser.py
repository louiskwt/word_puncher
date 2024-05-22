# Parser for files
import zipfile, re

class TextFileParser:
    def __init__(self, path):
        self.path = path

    def detect_file_type():
        pass
    
    def parse_txt_file(self):
        with open(self.path) as file:
            return [line.rstrip('\n') for line in file if line.rstrip('\n')]
    
    def parse_docx_file(self):
        with zipfile.ZipFile(self.path, 'r') as file:
            xml = file.read('word/document.xml')
        xml_str = xml.decode('utf-8')
        pattern = r'>(.*?)<'
        text = [s for s in re.findall(pattern, xml_str) if s and s!='\r']
        return text
