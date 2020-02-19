from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(30)

templeName = "Zu-Lin Temple Association"

# Open the page and search for the temple
driver.get("https://www.charities.gov.sg/Pages/Home.aspx")
searchField = driver.find_element_by_name(
    "ctl00$m$g_6c389038_955d_456d_901b_52f626b4cbba$ctl00$txtSearch")
searchField.send_keys(templeName)
searchBtn = driver.find_element_by_name(
    "ctl00$m$g_6c389038_955d_456d_901b_52f626b4cbba$ctl00$btnSearch")
searchBtn.click()

# confirm there is one and only one result for the search
resultsCount = driver.find_element_by_id(
    "ctl00_PlaceHolderMain_lblSearchCount")
assert "1 records found for" in resultsCount.text

# click on "View Details" button
viewDetailedBtn = driver.find_element_by_name(
    "ctl00$PlaceHolderMain$lstSearchResults$ctrl0$btnViewDetails")
viewDetailedBtn.click()

print('hello')
# click on "Financial Information"
fiTab = driver.find_element_by_link_text("Financial Information")
print(fiTab.text)
fiTab.click()

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
