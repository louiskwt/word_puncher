import pathlib
from text_file_parser import TextFileParser
from utils import punch_out_words


DIR = pathlib.Path(__file__).parent.resolve()

if __name__ == '__main__':
    filename = input("Enter a file name: ")  
    parser = TextFileParser(str(DIR) + '/' + filename)
    data = parser.parse_file()
    output, answers = punch_out_words(data)
    for line in output:
        print(output)
    print("________________Answer Keys____________________________________")
    print((", ".join(answers)))