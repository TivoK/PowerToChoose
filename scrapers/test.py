import re 

usage_pattern = '[0-9,]*\skWh|[0-9]*\skWh'
rate_pattern  = '[0-9]*\.[0-9]*¢|[0-9]*¢' 

class RateScrape:
    def __init__(self, soup):
        self.soup = soup
        #self. = None 
    
    def __repr__(self):
        return '<RateScrape>'

    @property
    def rate_table(self):
        return self.soup.find_all('tr', class_= 'row active')

    def get_company_name(self, element) -> str:
        """
        Returns the compnay from a Table row from bs4 Result set
        element 
        """
        #return the title attirbute and remove "Score Card" from name
        company = element.find('div',class_ = 'userratings')['title'].split('Scorecard')[0]
        return company

    def get_plan_name(self, element) -> str:
        """
        Returns the plan name from a Table row from bs4 Result set
        element 
        """
        plan_name = element.find('ul', class_ ='plan-info').find_all(
        'li',limit = 1)[0].string
        return plan_name
 
    def get_plan_attributes(self,element) ->dict:
        """
        Searches a grid to find the listed plan attributes
        """
        plan_attributes =dict()
        attributes = element.find_all('li',class_ ='grid-element')

        for num, attribute in enumerate(attributes, start=1):
            #remove html tags; format to string delete whitespace
            formatted_attribute = str(attribute.string).strip()
            #only store attributes that aren valid entries
            #note some attributes are listed as a string 'None'
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
        #select the elements with rate plan prices 
        prices = element.find('td' , class_ ='item td-price').find('div').contents
        #create empty lists to store findings
        usages =[]
        rates=[]
        
        for i in prices:
            #use regex to find usages listed as Kwh
            find_usage = re.findall(usage_pattern,str(i))
            #append finding to list
            usages.extend(find_usage)
            #use regex to find price listed in cents
            find_rate = re.findall(rate_pattern,str(i))
            #save to list
            rates.extend(find_rate)

        return dict(zip(usages,rates))



#pattern  = '[0-9]*\.[0-9]*¢|[0-9]*¢'  
#usage_pattern = '[0-9]*\skWh'
# test =['<div class="unit">500 kWh <span>10¢</span></div>', '<div class="unit">2000 kWh <span>8.8¢</span></div>']

# find = re.search(usage_pattern, test[0])

# print(find.group(0))


# find = re.search(pattern, test[0])

# print(find.group(0))