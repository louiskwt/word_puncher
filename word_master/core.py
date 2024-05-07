from text_file_parser import TextFileParser

if __name__ == '__main__':
    path = input("Enter a file path: ")
    print(path)   
    data = TextFileParser.parse_file(path)
    print(data)