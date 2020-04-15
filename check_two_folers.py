import os

pdf_foler = 'PDFs/'
church_folder = 'Churchs/'

pdfs = os.listdir(pdf_foler)
churchs = os.listdir(church_folder)

for item in churchs:
    if item + '.pdf' not in pdfs:
        print(item)