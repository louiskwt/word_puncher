from fpdf import FPDF

class PDF_Generator(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 14)
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width)/2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(width, 9, self.title, border=1, new_x="LMARGIN", new_y="NEXT", align="C", fill=True)
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "", 12)
        self.set_text_color(128)
        
    def set_body_heading(self, heading):
        self.set_font("helvetica", "", 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, heading, new_x="LMARGIN", new_y="NEXT", align="L", fill=True)
        self.ln(4)

    def print_page_content(self, heading, text):
        self.add_page()
        self.set_font("helvetica", size=12)
        self.set_body_heading(heading)
        self.multi_cell(0, 5, text)
        self.ln(4)
    