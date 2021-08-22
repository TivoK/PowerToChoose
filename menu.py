import os 
from datetime import datetime 

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



