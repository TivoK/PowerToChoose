
from selenium import webdriver
from bs4 import BeautifulSoup

from locators.homepage import HomePage
from pages.mainpage import PowerToChoose
#from scrapers.test import RatePageScraper

from locators.homepage import RatePlans
from bs4 import BeautifulSoup    


zipcode = input("Enter the zip code you are searching for Rates: ")
 
#print(type(zipcode))
#get the webdriver path
chrome = webdriver.Chrome(executable_path = './chromedriver/chromedriver.exe')
#go to webpage 
chrome.get('http://powertochoose.org')

Site = PowerToChoose(chrome)

Site.zipcode_entry(zipcode)

Site.view_rates.click()

html = Site.page #.browser.page_source

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

cb = Site.get_checkbox_status('cb1')
print(cb)

#print(chklist[0])

# for item in chklist[0]:
#     print(item)
# #print(type(chrome))
# print('\n\n\n\n\n\n')
# #print(chklist[1])
Site.select_show_all_plans()
Site.select_all_plantypes()
#Site.click_hidden_button('rm0')
#button1 = Site.browser.find_element_by_id('rm0')
#button1 = soup.find(attrs = {"id": "rm0"})
Site.view_all_plans

ss = Site.soup

sss =ss.find_all('tr', class_= 'row active')
company = sss[0].find('div',class_ = 'userratings')['title'].split('Scorecard')[0]
print(company)

print(sss[0].find('ul', class_ ='plan-info').find_all('li',class_ ='grid-element')[0].contents)



# ddd =BeautifulSoup(row, 'html.parser')

# print(ddd.select_one("userrating"))
# print(ddd.select("item td-plan"))
# print(ddd.select("item td-price"))


#userratings
#item td-plan
#'item td-price"