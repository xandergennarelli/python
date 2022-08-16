import tabula
import pandas as pd
import glob

files = glob.glob("pdf_out/*.pdf")

for file in files:  # read each file
    # df = tabula.read_pdf(str(file), area=(0,0,500,1035), guess=False, pages = 'all')  # guesses columns
    df = tabula.read_pdf(str(file), area=(0,0,500,1035), columns=(120,170,200,250,295,353,422,510,580,640,705,800,890,948), guess=False, pages = 'all')

    for i in range(len(df)):    # each page of file to a sheet
        df[i].to_excel('xlsx_out/' + str(file)[-8:-4] + '-' + str(i) +'.xlsx')