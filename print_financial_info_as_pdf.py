from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
import json


def download_imgs(urls, folder_name):
    '''
    Given a list of image URLs, download them to the folder folder_name.
    '''
    folder_name = folder_name.replace(':', '-')
    os.mkdir(folder_name)
    for i in range(len(urls)):
        file_name = urls[i].split('/')[-1].replace('%20', ' ')
        file_path = folder_name + '/' + file_name
        urllib.request.urlretrieve(urls[i], file_path)


SAVED_PDF = 'D:/Downloads/Organization Profile.pdf'
NEW_FOLDER = 'D:/GH/FinancialInfoFromCharityPortal/pdf_saves/'


def print_and_save_as_pdf(temple_name, info_type):
    driver.execute_script('window.print();')
    os.rename(SAVED_PDF, NEW_FOLDER + temple_name.replace(':', '') + info_type)
    # os.remove(SAVED_PDF)


def process_temple(temple_name):
    '''
    Search for the temple_name in the Charity Portal.
    Proceed to download the PDF images.
    '''
    searchField = driver.find_element_by_id("ctl00_PlaceHolderMain_txtSearch")
    searchField.clear()
    searchField.send_keys(temple_name)
    searchBtn = driver.find_element_by_id("ctl00_PlaceHolderMain_btnSearch")
    searchBtn.click()

    mainHandle = driver.current_window_handle
    print(mainHandle)

    # confirm there is one and only one result for the search
    resultsCount = driver.find_element_by_id(
        "ctl00_PlaceHolderMain_lblSearchCount")
    # assert "1 records found for" in resultsCount.text

    # click on "View Details" button

    # //*[@id="ctl00_PlaceHolderMain_lstSearchResults_ctrl0_lblNameOfOrg"]
    found_church = False
    for i in range(5):
        church_id = 'ctl00_PlaceHolderMain_lstSearchResults_ctrl' + str(
            i) + '_lblNameOfOrg'
        churchLabel = driver.find_element_by_id(church_id)
        if churchLabel.text.replace('.', '') == temple_name.replace('.', ''):
            found_church = True
            viewDetailedBtn = driver.find_element_by_id(
                "ctl00_PlaceHolderMain_lstSearchResults_ctrl" + str(i) +
                "_btnViewDetails")
            viewDetailedBtn.click()
            break
    if not found_church:
        print('search for church', temple_name, 'failed')
        return

    # viewDetailedBtn = driver.find_element_by_id(
    #     "ctl00_PlaceHolderMain_lstSearchResults_ctrl0_btnViewDetails")
    # viewDetailedBtn.click()

    # switch to the newly popped up window/tab
    driver.switch_to.window(driver.window_handles[1])
    # driver.switch_to_windows("Organisation Profile")
    # print Organisation Profile as PDF
    print_and_save_as_pdf(temple_name, '_OP.pdf')

    # click on "Financial Information"
    fiTab = driver.find_element_by_link_text("Financial Information")
    print(fiTab.text)
    fiTab.click()

    # dismiss the alert pormpt
    driver.switch_to.alert.accept()

    # click on "Financial Information" again
    fiTab = driver.find_element_by_link_text("Financial Information")
    print(fiTab.text)
    fiTab.click()

    # print Financial Information as profile
    print_and_save_as_pdf(temple_name, "_FI.pdf")

    driver.close()
    driver.switch_to.window(
        driver.window_handles[0])  # get back to the search page


chrome_options = webdriver.ChromeOptions()
settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": "",
    }],
    "selectedDestinationId":
    "Save as PDF",
    "version":
    2
}
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings)
}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')

driver = webdriver.Chrome(options=chrome_options)
# set the implicity wait time to as long as 300 seconds
# so that accidently long loading time of the web site
# won't break the program
driver.implicitly_wait(300)

# Open the page and search for the temple
driver.get(
    "https://www.charities.gov.sg/_layouts/MCYSCPSearch/MCYSCPSearchResultsPage.aspx"
)

with open('christianity.txt', 'r') as temple_list:
    for temple in temple_list:
        # ' '.join(temple.split()) to remove the trailing spaces and newline characters
        process_temple(' '.join(temple.split()))
        with open('print_as_pdf_done.txt', 'a+') as f:
            f.write(temple)

# close the browser window
driver.close()
driver.quit()
