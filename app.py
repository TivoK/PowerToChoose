
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
Site.all_plans.click()
Site.select_plan_type.click()
#Site.click_hidden_button('rm0')
#button1 = Site.browser.find_element_by_id('rm0')
#button1 = soup.find(attrs = {"id": "rm0"})
#print(button1)

#button1.click()

#Site.browser.execute_script("arguments[0].click();",button1)



#print(button1.parent.div.attrs['class'][1])
#print(button1.parent.div)


#resultsForm > div > aside > div.group-box > div:nth-child(5) > ul > li:nth-child(1) > div


#'//*[@id="resultsForm"]/div/aside/div[2]/div[5]/ul/li[1]/div'
#'//*[@id="resultsForm"]/div/aside/div[2]/div[5]/ul/li[2]/div'
#'//*[@id="resultsForm"]/div/aside/div[2]/div[6]/ul/li[3]/div'