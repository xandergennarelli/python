# Pdf mining

A series of scripts for mining data on Louisian domestic violence convictions from pdf tables for an investigative reporting project.

Uses PyPDF2, tabula, Pandas, openpyxl, glob, and progressbar.

## Usage

1. With unprocessed pdfs stored in pdf_in and MEC data in fixed, run pdfcrop.py to prepare the pdfs to be mined.
2. Run read.py, fix.py, and then combine.py.
3. The processed data will be in fixed/final.xlsx.
