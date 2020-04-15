from fpdf import FPDF
import os

churchs_dir = 'churchs/'
pdf_dir = 'PDFs/'

anchor = 'Abundant Grace Presbyterian Church'

churchlist = [
    'ABUNDANT LIFE FAMILY CHURCH LTD',
    'ADAM ROAD PRESBYTERIAN CHURCH',
    'AGAPE METHODIST CHURCH',
    'ALDERSGATE METHODIST CHURCH',
    'ALL GOOD GIFTS LTD',
    'ALL SAINTS MEMORIAL CHAPEL (SINGAPORE) LTD',
    'ALL SAINTS PRESBYTERIAN CHURCH',
    'AMAZING GRACE PRESBYTERIAN CHURCH',
    'AMBASSADORS FOR CHRIST (SINGAPORE) LIMITED',
    'ANG MO KIO CHINESE METHODIST CHURCH',
    'ANG MO KIO METHODIST CHURCH (TRAC)',
    'ANG MO KIO PRESBYTERIAN CHURCH',
    'ANG MO KIO TAMIL METHODIST CHURCH',
    'ARK, THE',
    'ARMENIAN APOSTOLIC CHURCH OF ST GREGORY THE ILLUMINATOR, TRUST, THE',
    'ASIA THEOLOGICAL CENTER',
]

# for church in os.listdir(churchs_dir):
# if church < anchor:
#     continue
for church in churchlist:
    church_dir = churchs_dir + '/' + church
    images = os.listdir(church_dir)

    if len(images) == 0:
        print(church, 'has no image files')
        continue

    pdf = FPDF()
    image_files = True
    for image in images:
        if not 'jpeg' in image.lower():
            image_files = False
            break
        pdf.add_page()
        pdf.image(church_dir + '/' + image, 0, 0, 210, 297)
    if not image_files:
        print(church, 'has wrong format files')
        continue
    pdf.output(pdf_dir + church + ".pdf", "F")