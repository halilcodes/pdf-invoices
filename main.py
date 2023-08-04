import pandas as pd
from fpdf import FPDF
import glob

pdf = FPDF(orientation="L", unit="mm", format="A4")
filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
