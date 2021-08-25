
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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
        """
        Enters in Zip Code into text box on Hompage
        """
        zip_text = HomePage.ZIPCODE
        element = self.browser.find_element_by_id(zip_text)
        element.send_keys(zipcode)
        return element.send_keys(Keys.RETURN)

    @property
    def view_rates(self):
        """
        Finds view rate button on homepage
        """     
        view_rates_button = HomePage.VIEWRATES
        element = self.browser.find_element_by_css_selector(view_rates_button)
        return element 

   

    @property
    def select_plan_dropdown(self) -> Select:
        """
        Returns a Select object for selection
        of plan type drop down
        """
        drop_down_xpath = RatePlans.ALLPLANDROPDOWN
        element = self.browser.find_element_by_xpath(drop_down_xpath)
        return Select(element)

    
    @property
    def view_all_plans(self):
        """
        Selects the view all plans in drop down box
        """
        self.select_plan_dropdown.select_by_visible_text(
            RatePlans.SEEALLPLANS)


    @property
    def current_url(self):
        """
        Returns current web url on Web Driver
        """
        return self.browser.current_url

    def click_button(self, xpath: str):
        """
        Generic method that can be leveraged to click 
        buttons.
        """     
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
        """
        Select multiple check boxes for plan types.
        """
        #xpaths in RatePlan class
        for xp in RatePlans.PLANS.values():
            #get the checkbox status and see what if its not checked..
            if self.get_checkbox_status(xp[1]) != 'chk-checked':
                #pass in the xpath
                self.click_button(xp[0]) 
        
    def select_show_all_plans(self):
        """
        Selects the raido button show all plans 
        """
        select_all_plans = PricingBilling.SHOWALLPLANS
        self.click_button(select_all_plans)

    def update_page(self):
        """
        Retrieves page source from Web Driver
        """
        #update the current page 
        self.page = self.browser.page_source


    @property
    def soup(self):
        """
        Returns a refreshed web page Beatuiful soup object.
        """
        #update the page 
        self.update_page()
        return BeautifulSoup(self.page, 'html.parser')


    def get_checkbox_status(self, id_name: str) ->str:
        """
        Returns the status of check boxes. 
        Checkboxes that are checked return 'chk-checked'
        
        """
        soup = self.soup
        cb = soup.find(attrs = {'id': id_name})
        #return the status id 
        return cb.parent.find('div').attrs['class'][1]

    
     
    def is_zip_not_found(self):
        """
        Returns a bool, if we find not found pop up 
        box for entered zips.
        """
        not_found = HomePage.ZIPNOTFOUND
        pop_up= self.browser.find_element_by_css_selector(not_found)
        return pop_up.is_displayed()

    def close_zip_not_found(self):
        """
        This closes the pop box that appears when a pop box 
        for a bad zip code appears.
        """
        xpath = HomePage.NOTFOUNDCLOSEXPATH
        self.click_button(xpath)


    def invalid_zip(self):
        """
        This checks to see if an error pop up box appears 
        when an invlaid zip code is entered on the site.
        """
        xpath = HomePage.NOTFOUNDCLOSEXPATH

        try:
            #maximum amount of time we want to wait is 10 secx
            element = WebDriverWait(self.browser, 5).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, xpath)
                )
            )

            return element.is_displayed()
        #if we cant find close box for invalid pop up then
        #rate is valid ie False
        except TimeoutException:
            return False 

    def navigate(self):
        """
        Performs actions for site navigation after a valid zip 
        code is entered. 
        """
        #clcks view rate button
        self.view_rates.click()
        #selects show all plans button
        self.select_show_all_plans()
        #clicks mult plan check boxes
        self.select_all_plantypes()
        #view all plans per page
        self.view_all_plans
                       
    
def zip_entry_length():
    """
    This prompts user to enter a zip of valid length.
    Also checks for non digit entries.
    """
    zipcode = input("Enter the zip code you are searching for Rates: ")

    while len(zipcode) != 5 or zipcode.isdigit() != True:
        
        message =str()
        error1 = ' Zip Code must be length of 5.'
        error2 = ' Zip Code must only contain numbers.'

        if len(zipcode) != 5:
            message +=error1
        if zipcode.isdigit() != True:
            message +=error2

        print(message)
        zipcode = input("Enter the zip code you are searching for Rates: ")
    
    return zipcode


class InvalidXPath(ValueError):
    pass 



        





    
