import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_no,Date = filename.split("-")
    # Adding invoice no in PDF header from csv
    pdf.set_font(family="Times",style="B",size=16)
    pdf.cell(w=0,h=10,txt=f"Invoice_no.{invoice_no}",ln=1)
    # Adding date in PDF header from csv
    pdf.set_font(family="Times",style="B",size=16)
    pdf.cell(w=0,h=10,txt=f"Date.{Date}",ln=1)
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
# Add header into table
    columns = df.columns
    columns = [item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", size=12,style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=40, h=8, txt=columns[1], border=1)
    pdf.cell(w=50, h=8, txt=columns[2], border=1)
    pdf.cell(w=40, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1,ln=1)
# Add table row
    for index,row in df.iterrows():
        pdf.set_font(family="Times", style="B", size=7)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]),border=1)
        pdf.cell(w=40, h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=50, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=40, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1,ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", style="B", size=7)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum sentence
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=40, h=8, txt=f"The total price is {total_sum}", ln=1)

    # Add company name and logo
    pdf.set_font(family="Times", size=16,style="B")
    pdf.cell(w=40, h=8, txt="PythonHow")
    pdf.image("image/pythonhow.png", w=10)

    pdf.output(f"PDFs/{filename}.pdf")



