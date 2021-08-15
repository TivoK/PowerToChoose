
import re
from selenium import webdriver
from bs4 import BeautifulSoup

from locators.homepage import HomePage
from pages.mainpage import PowerToChoose
#from scrapers.test import RatePageScraper

from locators.homepage import RatePlans
from bs4 import BeautifulSoup    
from scrapers.test import RateScrape

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

RateScraper = RateScrape(ss)
rate_data = RateScraper.rate_table

for row_num, row_data in enumerate(rate_data[0:3], start =1):
    print(f'plan: {row_num}')
    print(RateScraper.get_company_name(row_data))
    print(RateScraper.get_plan_name(row_data))
    print(f'plan att count: {RateScraper.get_plan_attributes_count(row_data)}')
    print(RateScraper.get_plan_attributes(row_data))
    print(RateScraper.get_plan_rates(row_data))
    print(RateScraper.get_all_attributes_names)
    print(RateScraper.get_all_usage_names)
    print(RateScraper.get_row_data(row_data))
    #print(RateScraper.create_data_dictionary())

df = RateScraper.to_datafame()
print(df.head())
# sss =ss.find_all('tr', class_= 'row active')


# print(f'sss type: {type(sss[0])}')

# company = sss[0].find('div',class_ = 'userratings')['title'].split('Scorecard')[0]
# print(company)
# #plan name
# print(sss[0].find('ul', class_ ='plan-info').find_all('li',limit = 1)[0].string)
# #plan length
# print(len(sss[0].find_all('li',class_ ='grid-element')))
# #plan_attributes
# plan_attr = sss[0].find_all('li',class_ ='grid-element')

# for attr in plan_attr:
#     pa = str(attr.string).strip()
#     if len(pa)>1 and pa !='None':   
#         print(pa)

# prices = sss[0].find('td' , class_ ='item td-price').find('div').contents

# usage_pattern = '[0-9,]*\skWh|[0-9]*\skWh'
# rate_pattern  = '[0-9]*\.[0-9]*¢|[0-9]*¢'  
# usages =[]
# rates=[]
# for i in prices:
#     #print(type(i))
#     #print(type(str(i)))
#     print(type(i.string))
#     find_usage = re.findall(usage_pattern,str(i))
#     print(find_usage)
#     usages.extend(find_usage)

#     find_rate = re.findall(rate_pattern,str(i))
#     print(find_rate)
#     rates.extend(find_rate)
    # if type(i.string) != 'NoneType':
    #     usages.append(find.group(0))


# #print(prices)
# print(usages)
# print(rates)
# print(dict(zip(usages,rates)))
#price2 = sss[0].find_all('div' , class_ ='unit').string
#print(price2)
#¢

# print(ddd.select_one("userrating"))
# print(ddd.select("item td-plan"))
# print(ddd.select("item td-price"))


#userratings
#item td-plan
#'item td-price"