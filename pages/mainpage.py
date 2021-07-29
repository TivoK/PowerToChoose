from typing import List 

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        #element = self.browser.find_element_by_css_selector(select_all_plans)
        element = self.browser.find_element_by_xpath(select_all_plans)

        return element 

    @property
    def select_plan_type(self):
        checkbox = RatePlans.PLANTYPE
        #element =  self.browser.find_element_by_css_selector(checkbox)
        element =  self.browser.find_element_by_xpath(checkbox)
        return element 


    @property
    def current_url(self):
        return self.browser.current_url


    def click_hidden_button(self, button_id: str):
        #maximum amount of time we want to wait is 10 secx
        WebDriverWait(self.browser, 60).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, button_id)
            )
        ).click()





        





    
