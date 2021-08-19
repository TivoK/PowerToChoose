
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


# zipcode = input("Enter the zip code you are searching for Rates: ")

# while len(zipcode) != 5:
#     print('Zip Code must be of 5 digit length.')
#     zipcode = input("Enter the zip code you are searching for Rates: ")
 
#get the entry...
zipcode = zip_entry_length()

#get the webdriver path
chrome = webdriver.Chrome(executable_path = './chromedriver/chromedriver.exe')
#go to webpage / open web browser
chrome.get('http://powertochoose.org')

Site = PowerToChoose(chrome)
#this passes in the 
Site.zipcode_entry(zipcode)

while Site.is_zip_not_found() == True:

        Site.browser.refresh()
        print("Zip Not Valid.")
       # Site.close_zip_not_found()
        rentry_zip = zip_entry_length()
        Site.zipcode_entry(rentry_zip)
    
    

 

#print(Site.browser)
#print(Site.is_zip_not_found())

#Site.view_rates.click()

#html = Site.page 

##################################################
#.browser.page_source

#print(Site.all_plans.is_displayed())
# Site.all_plans.click()

# Site.select_plan_type.click()
# Site.select_plan_type.click()

# #Site.select_plan_type.click()
# #Site.select_plan_type.click()
# #Site.select_plan_type.click()

# url = Site.current_url
# print(url)


#page = RatePageScraper(url).page

#soup = Site.soup#BeautifulSoup(html ,'html.parser')


#print(soup.prettify())

#cb = soup.find(attrs = {"id": "cb1"})
#print(cb.parent.find('div').attrs['class'][1])
#################################################################

# cb = Site.get_checkbox_status('cb1')
# print(cb)

# Site.select_show_all_plans()
# Site.select_all_plantypes()

# Site.view_all_plans

# ss = Site.soup

# RateScraper = RateScrape(ss)
# rate_data = RateScraper.rate_table

# for row_num, row_data in enumerate(rate_data[0:3], start =1):
#     print(f'plan: {row_num}')
#     print(RateScraper.get_company_name(row_data))
#     print(RateScraper.get_plan_name(row_data))
#     print(f'plan att count: {RateScraper.get_plan_attributes_count(row_data)}')
#     print(RateScraper.get_plan_attributes(row_data))
#     print(RateScraper.get_plan_rates(row_data))
#     print(RateScraper.get_all_attributes_names)
#     print(RateScraper.get_all_usage_names)
#     print(RateScraper.get_row_data(row_data))
#     #print(RateScraper.create_data_dictionary())

# df = RateScraper.to_datafame()
# print(df.head())
