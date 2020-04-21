from selenium import webdriver
import json

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
driver.get("https://google.com")
input('enter a number')
driver.switch_to.window(driver.window_handles[1])
driver.execute_script('window.print();')
driver.quit()