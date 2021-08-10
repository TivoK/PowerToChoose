import re 
class RateScrape:
    def __init__(self, parent):
        self.parent = parent
        self.row_html = None 
    
    def __repr__(self):
        return '<RateScrape>'

pattern  = '[0-9]*\.[0-9]*¢|[0-9]*¢'  
usage_pattern = '[0-9]*\skWh'
test =['<div class="unit">500 kWh <span>10¢</span></div>', '<div class="unit">2000 kWh <span>8.8¢</span></div>']

find = re.search(usage_pattern, test[0])

print(find.group(0))


find = re.search(pattern, test[0])

print(find.group(0))