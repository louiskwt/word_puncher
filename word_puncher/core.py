import pathlib
from os import path
from text_file_parser import TextFileParser
from utils import punch_out_words
from pdf_generator import PDF_Generator


DIR = pathlib.Path(__file__).parent.resolve()

if __name__ == '__main__':
    try:
        filename = input("Enter a file name: ") 
        filename = str(DIR) + '/' + filename
        valid_path = path.exists(filename)
        valid_file = path.exists(filename)
        if valid_file and valid_path:
            parser = TextFileParser(str(DIR) + '/' + filename)
            # docx_parser = TextFileParser(str(DIR) + '/' + filename)
            data = parser.parse_txt_file()
            output, answers = punch_out_words(data, 1)
            for line in output:
                print(line)
                print(("*" * 50) +  "Answer Keys" + ("*" * 50))
            print((", ".join(answers)))

            pdf = PDF_Generator()
            pdf.set_title("Listening Exercise With a Song")
            pdf.print_page_content(output[0], output[1:])
            answer_rows = [tuple(answers[i:i+4]) for i in range(len(answers)) if i % 4 == 0]  
            pdf.print_as_table("Answer Keys", answer_rows)
            pdf.output("test.pdf")
        else:
            raise FileExistsError
    except FileExistsError:
        print("Invalide File Input")


