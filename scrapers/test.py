import requests

class RatePageScraper:
    
    def __init__(self, url):
        self.page = requests.get(url).content 
    
    def get_content(self):
        return self.page



    