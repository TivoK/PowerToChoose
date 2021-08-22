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



#path = path_entry()

##name = save_as(path)
#print(name)