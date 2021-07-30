class HomePage:
    #get the name of the zip text box 
    ZIPCODE =   'homezipcode'
    VIEWRATES = 'a[id="view_all_results"]'
    FOUNDMSG =  'foundmessage'


class RatePlans:
    #Check box selectors
    PLANS = { 
        'INDEXPLAN' : '//*[@id="resultsForm"]/div/aside/div[2]/div[6]/ul/li[3]/div'
        ,'VARIABLEPLAN' : '//*[@id="resultsForm"]/div/aside/div[2]/div[6]/ul/li[2]/div'
        ,'FIXEDPLAN' : '//*[@id="resultsForm"]/div/aside/div[2]/div[6]/ul/li[1]/div'
    }


class PricingBilling:
    SHOWALLPLANS = '//*[@id="resultsForm"]/div/aside/div[2]/div[5]/ul/li[1]/div'
