
import re
from selenium import webdriver
from bs4 import BeautifulSoup

from locators.homepage import HomePage
from pages.mainpage import PowerToChoose, zip_entry_length
#from scrapers.test import RatePageScraper

from locators.homepage import RatePlans
from bs4 import BeautifulSoup    
from scrapers.test import RateScrape
from selenium.webdriver.common.alert import Alert
from menu import check_path


# zipcode = input("Enter the zip code you are searching for Rates: ")

# while len(zipcode) != 5:
#     print('Zip Code must be of 5 digit length.')
#     zipcode = input("Enter the zip code you are searching for Rates: ")
 
#get the entry...
#zipcode = zip_entry_length()

#get the webdriver path
chrome = webdriver.Chrome(executable_path = './chromedriver/chromedriver.exe')
#go to webpage / open web browser
chrome.get('http://powertochoose.org')

Site = PowerToChoose(chrome)
#this passes in the 
#Site.zipcode_entry(zipcode)

is_invalid_zipcode = None

while is_invalid_zipcode  != False:
    #Refresh the web-browser 
    #this is necessary if a bad zip code is passed;
    #will reset the pop up  to style: none 
    Site.browser.refresh()
    #check for length/non-digit entries...
    zipcode = zip_entry_length()

    Site.zipcode_entry(zipcode)
    #here we are checking if the 
    #bad zip pop up appears. 
    is_invalid_zipcode = Site.invalid_zip()
    #is_invalid_zipcode = Site.is_zip_not_found()  
    print(f'test loop: {is_invalid_zipcode}')
    
    if is_invalid_zipcode == True:
        print('Zip Code not Valid.')
   
 
 
#click needed web page elements 
Site.navigate()  
#get the HTML for site when all plans are shown
soup = Site.soup 

Rates = RateScrape(soup)

df_rates = Rates.to_datafame()

print(df_rates.head())

Site.browser.quit()

path = input('insert path to save file: ')

print(check_path(path))

