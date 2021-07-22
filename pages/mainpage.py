from typing import List 

class PowerToChoose:
    
    def __init__(self, browser):
        #pass in the browser we opened up
        self.browser = browser 
    
    #show the current url for the WebDriver class in repr
    def __repr__(self):
        return f"<selenium.webdriver.chrome.webdriver.WebDriver {self.browser.current_url}>"

    def zipcode_entry(self,int: zipcode):
        pass 

    
