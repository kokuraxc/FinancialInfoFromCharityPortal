from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request


def download_imgs(urls, folder_name):
    '''
    Given a list of image URLs, download them to the folder folder_name.
    '''
    FOLDER_NAME = 'pdf_saves'

    folder_name = FOLDER_NAME + '/' + folder_name.replace(':', '-')
    os.mkdir(folder_name)
    for i in range(len(urls)):
        file_name = urls[i].split('/')[-1].replace('%20', ' ')
        file_path = folder_name + '/' + file_name
        urllib.request.urlretrieve(urls[i], file_path)


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
        church_type = 'ctl00_PlaceHolderMain_lstSearchResults_ctrl' + str(
            i) + '_lblModule'
        church_type = driver.find_element_by_id(church_type)
        if (churchLabel.text.replace('.', '') == temple_name.replace(
                '.', '')) and church_type.text == 'Charity Organisation':
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

    # # Initially I want to handle the SingPass login page automatically, but then decided it
    # # doesn't worth the efforts, as I only need to login once for the first time to view
    # # the details of the financial information
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

    # check if financial reports are available
    receivedStatus = driver.find_element(
        By.XPATH,
        '//*[@id="ctl00_PlaceHolderMain_gvFinancialInformation"]/tbody/tr[2]/td[5]'
    )
    fileStatus = driver.find_element(
        By.XPATH,
        '//*[@id="ctl00_PlaceHolderMain_gvFinancialInformation"]/tbody/tr[2]/td[6]'
    )
    if receivedStatus.text == "Not received" or fileStatus.text == 'No file found':
        print(temple_name, 'has no fiancial reports', fileStatus.text,
              receivedStatus)
        driver.close()
        driver.switch_to.window(
            driver.window_handles[0])  # get back to the search page
        return

    # click on the "VIEW" button
    viewBtn = driver.find_element_by_id(
        "ctl00_PlaceHolderMain_gvFinancialInformation_ctl02_btViewload")
    viewBtn.click()

    # another windows will pop up
    driver.switch_to.window(driver.window_handles[2])

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
# set the implicity wait time to as long as 300 seconds
# so that accidently long loading time of the web site
# won't break the program
driver.implicitly_wait(300)

# Open the page and search for the temple
driver.get(
    "https://www.charities.gov.sg/_layouts/MCYSCPSearch/MCYSCPSearchResultsPage.aspx"
)

with open('Others.txt', 'r') as temple_list:
    for temple in temple_list:
        # ' '.join(temple.split()) to remove the trailing spaces and newline characters
        process_temple(' '.join(temple.split()))
        with open('downloaded.txt', 'a+') as f:
            f.write(temple)

# close the browser window
driver.close()
