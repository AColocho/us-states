import importlib.resources
import json

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

class Territories:
    with importlib.resources.path('data', "territories.json") as _data_file:
        _data = json.loads(_data_file.read_text())
    
    def get_territory_info(self,full_name):
        """
        Params: 
            full_name: The full name of the territory to search. If 'all' is passed, then it will
                        retrieve the full name of all territories.
            
        Returns:
            Dictionary with territory information when a territory name is passed.
            If 'all' is passed, then it will return the full name of territories in list form.
        """
        territory_data = self._data['territories']
        
        if full_name == 'all':
            territory_info = list(territory_data.keys())
            
        else:
            full_name = full_name.title()

            territory_info = territory_data.get(full_name, 
                        "Sorry try typing the name of the territory again, or pass 'all' for full_name to view all territories.")
        
        return territory_info