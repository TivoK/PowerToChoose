import re 
import logging
import pandas as pd


usage_pattern = '[0-9,]*\skWh|[0-9]*\skWh'
rate_pattern  = '[0-9]*\.[0-9]*¢|[0-9]*¢' 


logger = logging.getLogger('ScraperLog.scrape')

class RateScrape:
    def __init__(self, soup):
        self.soup = soup
        #self. = None 
    
    def __repr__(self):
        return '<RateScrape>'

    @property
    def rate_table(self):
        logger.debug('Find Rates Table on Web Page')
        return self.soup.find_all('tr', class_= 'row active')

    def get_company_name(self, element) -> dict:
        """
        Returns the compnay from a Table row from bs4 Result set
        element 
        """
        logger.debug('Getting Company Name')
        #return the title attirbute and remove "Score Card" from name
        company = element.find('div',class_ = 'userratings')['title'].split('Scorecard')[0]
        return {'CompanyName' : company}

    def get_plan_name(self, element) -> dict:
        """
        Returns the plan name from a Table row from bs4 Result set
        element 
        """
        logger.debug('Getting plan dictionary')
        plan_name = element.find('ul', class_ ='plan-info').find_all(
        'li',limit = 1)[0].string
        return {'Plan' : plan_name}
 
    def get_plan_attributes(self,element) ->dict:
        """
        Searches a grid to find the listed plan attributes
        """
        plan_attributes =dict()
        logger.debug('Find Plan Attributes')
        attributes = element.find_all('li',class_ ='grid-element')
        logger.debug('Iterate through Plan Attribute Grid')
        for num, attribute in enumerate(attributes, start=1):
            #remove html tags; format to string delete whitespace
            formatted_attribute = str(attribute.string).strip()
            #only store attributes that aren valid entries
            #note some attributes are listed as a string 'None'
            logger.debug('Format Plan Attribute')
            if len(formatted_attribute)>1 and formatted_attribute !='None':   
                attribute_name  = "Plan_Attribute"+str(num)
                #save attribute to dict
                plan_attributes[attribute_name] = formatted_attribute

        return plan_attributes
       
    def get_plan_attributes_count(self,element) -> int:
        """
        Returns count of valid attibutes in a plan 
        """
        plan_attributes = element.find_all('li',class_ ='grid-element')
        counter = 0
        for attribute in plan_attributes:
            formatted_attribute = str(attribute.string).strip()
            #only count attributes that aren valid entries
            #note some attributes are listed as a string 'None'
            if len(formatted_attribute)>1 and formatted_attribute !='None': 
                counter+=1

        return counter

    def get_plan_rates(self, element) -> dict:
        """
        Returns a dictionary with Plan Prices based on usage tiers
        """
        logger.debug('Find Rate Prices')
        #select the elements with rate plan prices 
        prices = element.find('td' , class_ ='item td-price').find('div').contents
        #create empty lists to store findings
        usages =[]
        rates=[]
        
        for i in prices:
            logger.debug('Get Usgae with Regex')
            #use regex to find usages listed as Kwh
            find_usage = re.findall(usage_pattern,str(i))
            #append finding to list
            usages.extend(find_usage)
            logger.debug('Get Rate with Regex')
            #use regex to find price listed in cents
            find_rate = re.findall(rate_pattern,str(i))
            #save to list
            rates.extend(find_rate)

        return dict(zip(usages,rates))

    @property
    def get_all_attributes_names(self) -> list:
        """
        iterates through all the rows of the Rate table 
        and sees how many differnt attributes are listed. 
        this will utilized when creating dataframe column names.. 
        """
        rate_table = self.rate_table
        name_list = list()
        logger.debug('Get Attribute Names')
        for row in rate_table:
            names = self.get_plan_attributes(row).keys()
            name_list.extend(names)
        return sorted(set(name_list))

    @property    
    def get_all_usage_names(self) -> list:
        """
        iterates through all the rows of the Rate table 
        and sees how many differnt usage tiers are listed for each
        rate plan..  
        """
        rate_table = self.rate_table
        rate_list = list()
        logger.debug('Get Usage Names')
        for row in rate_table:
            rates = self.get_plan_rates(row).keys()
            rate_list.extend(rates)
        return sorted(set(rate_list))
            
    
    def create_data_dictionary_columns(self) -> list:
        """
        creates a list with column names .
        """
        logger.debug('Create Dictionary columns for DataFrame')
        columns = ['CompanyName','Plan']
        columns.extend(self.get_all_usage_names)
        columns.extend(self.get_all_attributes_names)
        return columns 
        
    def get_row_data(self,element) -> dict:
        """
        returns a dictinary for a single table row in the parsed
        data table from PowerToChoose site.
        """
        logger.debug('Create Row Data for DataFrame')
        #get the column names we in our dictionary
        return_data = dict().fromkeys(self.create_data_dictionary_columns())
        #get the data from the row we are extracting 
        row_data = self.get_company_name(element)
        #append other data points to row_data
        row_data.update(self.get_plan_name(element))    
        row_data.update(self.get_plan_rates(element))
        row_data.update(self.get_plan_attributes(element))
        
        #update return data
        for column in return_data.keys():
            if column in row_data:
                return_data[column] = row_data[column]

        return return_data

    def to_datafame(self):
        """
        Creates Pandas DataFrame
        """
        logger.debug('Create DataFrame')
        rate_table = self.rate_table
        row_list = list()
        for row in rate_table:
            data = self.get_row_data(row)
            row_list.append(data)

        return pd.DataFrame(row_list)

