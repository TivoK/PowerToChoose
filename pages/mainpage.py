from typing import List 

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from locators.homepage import HomePage, RatePlans, PricingBilling


class PowerToChoose:
    
    def __init__(self, browser):
        #pass in the browser we opened up
        self.browser = browser 
        self.page = browser.page_source
    
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

    @property
    def select_plan_dropdown(self) -> Select:
        drop_down_xpath = RatePlans.ALLPLANDROPDOWN
        element = self.browser.find_element_by_xpath(drop_down_xpath)
        return Select(element)

    
    @property
    def view_all_plans(self):
        self.select_plan_dropdown.select_by_visible_text(
            RatePlans.SEEALLPLANS)
        #self.select_all_plans.select_by_visible_text(RatePlan.SEEALLPLANS)

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
                f'XPATH: "{xpath}" was not found.'
            )
        

    def select_all_plantypes(self):
        #xpaths in RatePlan class
        for xp in RatePlans.PLANS.values():
            #get the checkbox status and see what if its not checked..
            if self.get_checkbox_status(xp[1]) != 'chk-checked':
                #pass in the xpath
                self.click_button(xp[0]) 
        
    def select_show_all_plans(self):
        #select the raido button show all plans 
        select_all_plans = PricingBilling.SHOWALLPLANS
        self.click_button(select_all_plans)

    def update_page(self):
        #update the current page 
        self.page = self.browser.page_source


    @property
    def soup(self):
        #update the page 
        self.update_page()
        return BeautifulSoup(self.page, 'html.parser')


    def get_checkbox_status(self, id_name: str) ->str:
        soup = self.soup
        cb = soup.find(attrs = {'id': id_name})
        #return the status id 
        return cb.parent.find('div').attrs['class'][1]


    
        


class InvalidXPath(ValueError):
    pass 



        





    
