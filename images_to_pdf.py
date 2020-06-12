from fpdf import FPDF
import os
import pprint

org_family_dir = 'pdf_saves/'

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

org_family_list = os.listdir(org_family_dir)
for org_family in org_family_list:
    org_list = os.listdir(org_family_dir + org_family + '/')
    pprint.pprint(org_list)

    # for church in os.listdir(churchs_dir):
    # if church < anchor:
    #     continue
    for org in org_list:
        org_dir = org_family_dir + org_family + '/' + org + '/'
        images = os.listdir(org_dir)

        if len(images) == 0:
            print(org, 'has no image files')
            continue

        pdf = FPDF()
        image_files = True
        for image in images:
            if not 'jpeg' in image.lower():
                image_files = False
                break
            pdf.add_page()
            pdf.image(org_dir + image, 0, 0, 210, 297)
        if not image_files:
            print(org, 'has wrong format files')
            continue
        pdf.output(org_family_dir + org_family + '/' + org + ".pdf", "F")