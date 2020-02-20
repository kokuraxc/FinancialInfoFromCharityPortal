from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request


def download_imgs(urls, folder_name):
    os.mkdir(folder_name)
    for i in range(len(urls)):
        file_name = urls[i].split('/')[-1].replace('%20', ' ')
        file_path = folder_name + '/' + file_name
        urllib.request.urlretrieve(urls[i], file_path)


def process_temple(temple_name):
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

    viewDetailedBtn = driver.find_element_by_id(
        "ctl00_PlaceHolderMain_lstSearchResults_ctrl0_btnViewDetails")
    viewDetailedBtn.click()

    # switch to the newly popped up window/tab
    driver.switch_to.window(driver.window_handles[1])
    # driver.switch_to_windows("Organisation Profile")

    # click on "Financial Information"
    fiTab = driver.find_element_by_link_text("Financial Information")
    print(fiTab.text)
    fiTab.click()

    driver.switch_to.alert.accept()

    # click on "Financial Information" again
    fiTab = driver.find_element_by_link_text("Financial Information")
    print(fiTab.text)
    fiTab.click()

    # # handle alert
    # try:
    #     WebDriverWait(driver, 2).until(EC.alert_is_present(),
    #                                    "Timed out waiting for SingPass login")
    #     driver.switch_to.alert.accept()

    #     # now in singpass login page.
    #     # toggle the qr code display
    #     qrtoggle = driver.find_element_by_id("qrcodeloginli")
    #     qrtoggle.click()

    #     # now login from the SingPass Mobile app

    #     # get back to the browser
    #     # click on "Financial Information"
    #     fiTab = driver.find_element_by_link_text("Financial Information")
    #     print(fiTab.text)
    #     fiTab.click()
    # finally:
    #     print("No alert to login SingPass")

    # click on the "VIEW" button
    viewBtn = driver.find_element_by_id(
        "ctl00_PlaceHolderMain_gvFinancialInformation_ctl02_btViewload")
    viewBtn.click()

    # another windows will pop up
    driver.switch_to.window(driver.window_handles[2])

    # for img in driver.find_elements_by_tag_name('img'):
    #     print(img.get_attribute("src"))
    # get the pdf imgs' urls
    # the last image in this page is the MCCY logo, so get rid of it.
    pdf_imgs = driver.find_elements_by_tag_name('img')[:-1]
    pdf_imgs = [img.get_attribute("src") for img in pdf_imgs]

    download_imgs(pdf_imgs, temple_name)

    # when downloading is done, close the two popped up windows
    driver.close()  # closed the pdf page
    driver.switch_to.window(
        driver.window_handles[1])  # close the organization profile page
    driver.close()

    driver.switch_to.window(
        driver.window_handles[0])  # get back to the search page


driver = webdriver.Chrome()
driver.implicitly_wait(300)

# Open the page and search for the temple
driver.get(
    "https://www.charities.gov.sg/_layouts/MCYSCPSearch/MCYSCPSearchResultsPage.aspx"
)

with open('temple_list.txt', 'r') as temple_list:
    for temple in temple_list:
        process_temple(' '.join(temple.split()))
        with open('downloaded.txt', 'a+') as f:
            f.write(temple)

driver.close()
