# FinancialInfoFromCharityPortal
This Python program will download the latest Financial Information of the *Buddhist* and *Taoist* temples that Ranran's doing research on from [the Charity Portal](https://www.charities.gov.sg/Pages/Home.aspx) website by Ministry of Culture, Community and Youth, Singapore.

The program was written with `Python` and [`Selenium`](https://selenium-python.readthedocs.io/index.html).

The program works like this:

1. Reads the temple names from the list from the `temple_list.txt` file.
2. Starts an instance of Chrome browser, opens the search page in the Charity Portal website.
3. For every temple name
    1. Inputs the temple name to the search field, clicks Search button.
    2. In the results page, clicks on the "VIEW DETAILS" button.
    3. A new page pops up, clicks on the "Financial Information" tab.
    4. An alert will pop up, clicks "OK" button.
        * For the first temple, it will ask to login with SingPass. It will direct the browser to SingPas login page, the user needs to login their credentials.
    5. Clicks on the "Financial Information" tab again.
    6. Clicks on the "VIEW" button.
    7. The financial infomation will be displayed in a new page.
    8. Gets the URLs for all the images and download them with `urllib.request.urlretrieve`.
    9. Closes the two popped up windows.

Except for the SingPass login process which requires human interaction, all the other steps are carried out automatially, thanks to `Selenium`.

With this script, I downloaded 104 Buddhist and Taoist temples' financial reports from the Charity Portal website. 
    