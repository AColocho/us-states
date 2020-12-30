class Territories_Abbreviated:
    atlantic = ['PR','VI']
    pacific = ['AS','GU','MP']
    
    all_territories = []
    all_territories.extend(atlantic + pacific)
    
class Territories_Full_Name:
    atlantic = ['Puerto Rico', 'U.S Virgin Islands']
    pacific = ['American Samoa', 'Guam', 'Northern Mariana Islands']
    
    all_territories = []
    all_territories.extend(atlantic + pacific)
    
class Associated_States:
    pacific_abbreviated = ['FM','PW', 'MH']
    pacific_full_name = ['Federated States of Micronesia','Republic of Palau', 'Marshall Islands']

class Uninhabited_Territories:
    all_territories = ['Baker Island', 'Howland Island', 'Johnston Atoll', 'Kingman Reef', 'Midway Island',
                       'Navassa Island', 'Palmyra Atoll']