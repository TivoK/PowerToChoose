from typing import List 

from selenium.webdriver.common.keys import Keys
from locators.homepage import HomePage, RatePlans


class PowerToChoose:
    
    def __init__(self, browser):
        #pass in the browser we opened up
        self.browser = browser 
    
    #show the current url for the WebDriver class in repr
    def __repr__(self):
        return f"<selenium.webdriver.chrome.webdriver.WebDriver {self.browser.current_url}>"

    
    def zipcode_entry(self, zipcode: str):
        #get the locator for textbox for zipocde entry
        zip_text = HomePage.ZIPCODE
        element = self.browser.find_element_by_id(zip_text)
        element.send_keys(zipcode)
        return element.send_keys(Keys.RETURN)

    @property
    def view_rates(self):
        #find button for clikcing rates
        view_rates_button = HomePage.VIEWRATES
        element = self.browser.find_element_by_css_selector(view_rates_button)
        return element 
        #element.click()

    @property
    def all_plans(self):
        
        select_all_plans = RatePlans.PRICINGANDBILLING
        element = self.browser.find_element_by_css_selector(select_all_plans)
        return element 



        





    
