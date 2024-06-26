from fpdf import FPDF
from fpdf.fonts import FontFace
import pathlib

DIR = pathlib.Path(__file__).parent.resolve()

class PDF_Generator(FPDF):
    """ PDF_Generator handles the pdf generation process """
    def header(self):
        self.add_font('roboto', style="B", fname=str(DIR) + "/fonts/Roboto/Roboto-Bold.ttf")
        self.set_font("roboto", "B", 14)
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width)/2)
        self.set_text_color(0, 50, 50)
        self.set_line_width(1)
        self.cell(width, 9, self.title, border=0, new_x="LMARGIN", new_y="NEXT", align="C")
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("roboto", "", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="R")
        self.ln(5)
        self.cell(0, 5, 'Created By kawingz', align="C")
        
    def set_body_heading(self, heading):
        self.set_font("roboto", "", 12)
        self.cell(0, 6, heading, new_x="LMARGIN", new_y="NEXT", align="L")
        self.ln(4)

    def print_page_content(self, heading, text):
        self.add_page()
        self.add_font('roboto', style="", fname=str(DIR) + "/fonts/Roboto/Roboto-Regular.ttf")
        self.set_font("roboto", size=12)
        self.set_body_heading(heading)
        for line in text:
            self.multi_cell(0, 5, text=line)
            self.ln(7.5)

    def print_as_table(self, heading, text):
        self.add_page()
        self.set_font("roboto", size=12)
        self.set_body_heading(heading)
        data_table = Table()
        for line in text:
            data_table.add_row(line)

        with self.table(headings_style = FontFace(emphasis=None)) as pdf_table:
            for data_row in data_table.rows:
                row = pdf_table.row()
                for datum in data_row:
                    row.cell(datum) 



class Table:
    '''Custom Data Structure for PDF table rows'''
    empty = ()
    rows = ()
    
    def add_row(self, row):
        assert row is not self.empty
        self.rows = self.rows + (row, )
