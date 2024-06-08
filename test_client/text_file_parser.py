# Parser for files
import zipfile, re

class TextFileParser:
    def __init__(self, path):
        self.path = path
        self.parse = self.parse_txt_file 

    def detect_file_type(self):
        EXTENSION_SIGNATURE = {
            "docx": "50 4B 03 04",
        }
        file = open(self.path, "rb").read(32)
        file_hex_numbers = " ".join(['{:02X}'.format(byte) for byte in file])[:11]
        print(file_hex_numbers)
        for _, val in EXTENSION_SIGNATURE.items():
            if file_hex_numbers == val:
                self.parse = self.parse_docx_file
        
    
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
