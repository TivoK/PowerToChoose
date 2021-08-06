class HomePage:
    #get the name of the zip text box 
    ZIPCODE =   'homezipcode'
    VIEWRATES = 'a[id="view_all_results"]'
    FOUNDMSG =  'foundmessage'


class RatePlans:
    #Check box selectors xpaths and ids 
    PLANS = { 
        'INDEXPLAN' : ('//*[@id="resultsForm"]/div/aside/div[2]/div[6]/ul/li[3]/div' , 'cb3')
        ,'VARIABLEPLAN' : ('//*[@id="resultsForm"]/div/aside/div[2]/div[6]/ul/li[2]/div','cb2')
        ,'FIXEDPLAN' : ('//*[@id="resultsForm"]/div/aside/div[2]/div[6]/ul/li[1]/div','cb1')
    }
    #XPATH FOR DROP DOWN
    ALLPLANDROPDOWN = '//*[@id="pagesize"]'
    #tag name for all plans in drop down
    SEEALLPLANS = 'SEE ALL'

class PricingBilling:
    SHOWALLPLANS = '//*[@id="resultsForm"]/div/aside/div[2]/div[5]/ul/li[1]/div'
