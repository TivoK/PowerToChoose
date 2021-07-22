from selenium import webdriver

from locators.homepage import HomePage
from pages.mainpage import PowerToChoose

zipcode = input("Enter the zip code you are searching for Rates: ")
 
#get the webdriver path
chrome = webdriver.Chrome(executable_path = './chromedriver/chromedriver.exe')
#go to webpage 
chrome.get('http://powertochoose.org')

Site = PowerToChoose(chrome)



#print(type(chrome))


