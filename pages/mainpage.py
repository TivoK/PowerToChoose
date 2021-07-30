from typing import List 

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys
from locators.homepage import HomePage, RatePlans, PricingBilling


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

    # @property
    # def all_plans(self):
    #     #select the show all plans  
    #     select_all_plans = PricingBilling.SHOWALLPLANS
    #     element = self.browser.find_element_by_xpath(select_all_plans)
    #     return element 

    # @property
    # def select_plan_type(self):
    #     checkbox = RatePlans.PLANTYPE
    #     #element =  self.browser.find_element_by_css_selector(checkbox)
    #     element =  self.browser.find_element_by_xpath(checkbox)
    #     return element 

    @property
    def current_url(self):
        return self.browser.current_url


    def click_button(self, xpath: str):
        try:
             #maximum amount of time we want to wait is 10 secx
            WebDriverWait(self.browser, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, xpath)
                )
            ).click()
        #raise custom xpath error 
        except NoSuchElementException:
            raise InvalidXPath(
                f'XPATH: "{xpaht}" was not found.'
            )
        

    def select_all_plantypes(self):
        #xpaths in RatePlan class
        for xp in RatePlans.PLANS.values():
            self.click_button(xp) 
        
    def select_show_all_plans(self):
        #select the raido button show all plans 
        select_all_plans = PricingBilling.SHOWALLPLANS
        self.click_button(select_all_plans)
        


class InvalidXPath(ValueError):
    pass 



        





    
