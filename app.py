
from selenium import webdriver
from bs4 import BeautifulSoup

from locators.homepage import HomePage
from pages.mainpage import PowerToChoose
from scrapers.test import RatePageScraper



zipcode = input("Enter the zip code you are searching for Rates: ")
 
#print(type(zipcode))
#get the webdriver path
chrome = webdriver.Chrome(executable_path = './chromedriver/chromedriver.exe')
#go to webpage 
chrome.get('http://powertochoose.org')

Site = PowerToChoose(chrome)

Site.zipcode_entry(zipcode)

Site.view_rates.click()

html = Site.browser.page_source

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

soup = BeautifulSoup(html ,'html.parser')


#print(soup.prettify())

chklist = soup.find_all('ul',class_ = 'check-list')
#print(chklist[0])

# for item in chklist[0]:
#     print(item)
# #print(type(chrome))
# print('\n\n\n\n\n\n')
# #print(chklist[1])

button1 = soup.find(attrs = {"id": "rm0"})
print(button1)

print(button1.parent.div.attrs['class'][1])