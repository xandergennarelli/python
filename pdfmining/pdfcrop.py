wfrom PyPDF2 import PdfWriter, PdfReader
import glob

left = 30
top = 30      # 80
width = 1035
height = 500  # 450

files = glob.glob("pdf_in/*.pdf")

for file in files:
  reader = PdfReader(file)
  writer = PdfWriter()

  oldHeight = reader.pages[0].cropbox.upper_right[1]

  count = 0

  for page in reader.pages:
    if count == 0:
      page.cropbox.upper_left = (left, oldHeight - 80)
      page.cropbox.lower_right = (width + left, oldHeight - (450 + 80))
    else:
      page.cropbox.upper_left = (left, oldHeight - top)
      page.cropbox.lower_right = (width + left, oldHeight - (height + top))
    writer.add_page(page)
    count += 1
    
  with open('pdf_out/' + str(file)[-8:],'wb') as fp:
    writer.write(fp) 