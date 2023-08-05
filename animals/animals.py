from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("*.txt")
# print(filepaths)

for path in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    header = path.split(".")[0].capitalize()
    print(header)
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt=header, align="L", ln=1)
    with open(path, "r") as file:
        text = file.read()
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=10, txt=text)

    pdf.output(f"{header.lower()}.pdf")