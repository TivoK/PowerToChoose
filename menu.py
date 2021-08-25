import os 
from datetime import datetime
from selenium import webdriver
from scrapers.scrape import RateScrape
from pages.mainpage import PowerToChoose, zip_entry_length

 

def check_path(path: str) ->bool:
    # Check whether the  
    # specified path is an 
    # existing directory or not 
    isdir = os.path.isdir(path) 
    return isdir  

def path_entry() -> str:
    """
    Asks user for path to save scraped data frame. Returns valid
    string path.
    """
    path = input('Insert Path to Folder to save results: ')
    is_valid_dir = check_path(path)
    
    while is_valid_dir != True:
        print(f'Invalid Directory: {path}')
        path = input('Insert Path to Folder to save results: ')
        is_valid_dir = check_path(path)

    return path 

def get_current_date() ->str:
    """
    Returns YYYYMMDD_HHMM fto save 
    """
    current_date = datetime.now()
    name = current_date.strftime("%Y%m%d_%H%M")
    return name 

def save_as(path: str, df):
    """
    Prompts user to make selection to save dataframe 
    as Excel or CSV file & create path to save file.
    """
    message ='Save file as Excel Document or CSV File? \
             \nType (1) for Excel or (2) CSV File: '
    file_type = input(message)

    while file_type not in ('1','2'):
        print("Type (1) for Excel or (2) CSV File")
        file_type = input(message)

    if file_type == '1':
        excel = path + '/' + 'RATES_' + get_current_date() + '.xlsx'
        df.to_excel(excel, index = False)
    else:   
        csv =  path + '/' + 'RATES_' + get_current_date() + '.csv'
        df.to_csv(csv, index = False)


def scrape_rates():
    """ 
    This function will navigate site and pull output a CSV
    or a Excel file of the rates for a given Texas Zip Code.
    """

    #get the webdriver path
    chrome = webdriver.Chrome(executable_path = './chromedriver/chromedriver.exe')
    
    #go to webpage / open web browser
    chrome.get('http://powertochoose.org')

    Site = PowerToChoose(chrome)
    
    #loop until we enter valid zip code in texas
    is_invalid_zipcode = None

    while is_invalid_zipcode  != False:
        #Refresh the web-browser 
        #this is necessary if a bad zip code is passed;
        #will reset the pop up  to style: none 
        Site.browser.refresh()
        #check for length/non-digit entries...
        zipcode = zip_entry_length()

        Site.zipcode_entry(zipcode)
        #here we are checking if the 
        #bad zip pop up appears. 
        is_invalid_zipcode = Site.invalid_zip()
         
        if is_invalid_zipcode == True:
            print('Zip Code not Valid.')
    
    print('Navigating...')           
    #click needed web page elements 
    Site.navigate()  
    
    #get the HTML for site when all plans are shown
    soup = Site.soup 
    
    #pass into RateScape
    Rates = RateScrape(soup)

    print('Starting Scrape...')
    
    df_rates = Rates.to_datafame()
    #closes the browser after dataframe created
    Site.browser.quit()

    #save dataframe to correct path
    path = path_entry()
    save_as(path, df_rates)

    print('Complete!')
