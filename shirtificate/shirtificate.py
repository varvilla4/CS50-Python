from fpdf import FPDF


class get_PDF():
    def __init__(self, name):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 45)
        pdf.cell(0, 57, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=0, y=70)
        pdf.set_font_size(30)
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 213, f"{name} took CS50", align="C", center=True)
        pdf.output("shirtificate.pdf")

name = input("Name: ")
pdf = get_PDF(name)
