import pandas as pd
import glob
#from fpdf import fpdf

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    print(df)



