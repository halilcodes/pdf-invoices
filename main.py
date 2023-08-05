import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    # pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    # absolute_path = filepath[9:-5]    # 1001-2023.1.18
    absolute_path = Path(filepath).stem     # 1001-2023.1.18

    invoice_no = absolute_path.split("-")[0].strip()
    invoice_date = absolute_path.split("-")[1].strip()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=10, txt=f"Invoice nr. {invoice_no}", align="L", ln=1)
    pdf.cell(w=0, h=10, txt=f"Date {invoice_date}", align="L", ln=1)

    # set table headers
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="Product ID", border=1)
    pdf.cell(w=60, h=8, txt="Product Name", border=1)
    pdf.cell(w=30, h=8, txt="Amount", border=1)
    pdf.cell(w=40, h=8, txt="Price per Unit", border=1)
    pdf.cell(w=30, h=8, txt="Total Price", border=1, ln=1)
    grand_total = 0

    # filling the table
    for _, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        amount = row['amount_purchased']
        price = row["price_per_unit"]
        total = round(amount * price, 2)
        grand_total += total
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=30, h=8, txt=str(amount), border=1)
        pdf.cell(w=40, h=8, txt=str(price), border=1)
        pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)
    # insert grand total line
    pdf.cell(w=30, h=8, txt=str(), border=1)
    pdf.cell(w=60, h=8, txt=str(), border=1)
    pdf.cell(w=30, h=8, txt=str(), border=1)
    pdf.cell(w=40, h=8, txt=str(), border=1)
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=str(grand_total), border=1, ln=1)

    # create some space
    pdf.cell(w=30, h=30, txt=str(), ln=1)
    # last two lines
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=10, txt=f"The total amount is {grand_total} Euros.", align="L", ln=1)
    pdf.cell(w=0, h=10, txt=f"Designed by Halil Can Hasmer.", align="L", ln=1)
    pdf.output(f"PDFs/{absolute_path}.pdf")
