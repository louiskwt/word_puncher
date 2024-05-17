import pathlib
from text_file_parser import TextFileParser
from utils import punch_out_words
from pdf_generator import PDF_Generator


DIR = pathlib.Path(__file__).parent.resolve()

if __name__ == '__main__':
    filename = input("Enter a file name: ")  
    parser = TextFileParser(str(DIR) + '/' + filename)
    data = parser.parse_file()
    output, answers = punch_out_words(data)
    for line in output:
        print(line)
    print(("*" * 50) +  "Answer Keys" + ("*" * 50))
    print((", ".join(answers)))

    pdf = PDF_Generator()
    pdf.set_title("Listening Exercise With a Song")
    pdf.print_page_content(output[0], "\n".join(output[1:]))
    pdf.print_page_content("Answer Keys", "\n".join(answers))
    pdf.output("test.pdf")
