from . import data

class States_Abbreviated:
    def __init__(self, is_DC_state):
        if not is_DC_state:
           self.south_atlantic.remove('DC')
           self.all_states.remove('DC')
           self.south_region.remove('DC')
           
    east_north_central = ['IL', 'IN', 'MI', 'OH', 'WI']
    
    east_south_central = ['AL', 'KY', 'MS', 'TN']
    
    mid_atlantic = ['NJ', 'NY', 'PA']
    
    mountain = ['AZ', 'CO', 'ID', 'MT', 'NM', 'NV', 'UT', 'WY']
    
    new_england = ['CT', 'MA', 'ME', 'NH', 'RI', 'VT']
    
    pacific = ['AK', 'CA', 'HI', 'OR', 'WA']
    
    south_atlantic = ['DC', 'DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'WV']
    
    west_north_central = ['IA', 'KS', 'MIN', 'MO', 'ND', 'NE', 'SD']
    
    west_south_central = ['AR', 'LA', 'OK', 'TX']
    
    all_states = []
    all_states.extend(east_north_central + east_south_central + mid_atlantic
                      + mountain + new_england + pacific + south_atlantic
                      + west_north_central + west_south_central)
    
    northeast_region = []
    northeast_region.extend(new_england + mid_atlantic)
    
    midwest_region = []
    midwest_region.extend(east_north_central + west_north_central)
    
    south_region = []
    south_region.extend(south_atlantic + east_south_central + west_south_central)
    
    west_region = []
    west_region.extend(mountain + pacific)  
    
class States_Full_Name:
    def __init__(self, DC_Statehood):
        if not DC_Statehood:
           self.south_atlantic.remove('District of Columbia')
           self.all_states.remove('District of Columbia')
           self.south_region.remove('District of Columbia')
           
    east_north_central = ['Illinois', 'Indiana', 'Michigan', 'Ohio', 'Wisconsin']
    
    east_south_central = ['Alabama', 'Kentucky', 'Mississippi', 'Tennessee']
    
    mid_atlantic = ['New Jersey', 'New York', 'Pennsylvania']
    
    mountain = ['Arizona', 'Colorado', 'Idaho', 'Montana', 'New Mexico', 'Nevada', 'Utah', 'Wyoming']
    
    new_england = ['Connecticut', 'Massachusetts', 'Maine', 'New Hampshire', 'Rhode Island', 'Vermont']
    
    pacific = ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington']
    
    south_atlantic = ['District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Maryland', 'North Carolina', 'South Carolina', 'Virginia', 'West Virginia']
    
    west_north_central = ['Iowa', 'Kansas', 'Minnesota', 'Missouri', 'North Dakota', 'Nebraska', 'South Dakota']
    
    west_south_central = ['Arkansas', 'Louisiana', 'Oklahoma', 'Texas']
    
    all_states = []
    all_states.extend(east_north_central + east_south_central + mid_atlantic
                      + mountain + new_england + pacific + south_atlantic
                      + west_north_central + west_south_central)
    
    northeast_region = []
    northeast_region.extend(new_england + mid_atlantic)
    
    midwest_region = []
    midwest_region.extend(east_north_central + west_north_central)
    
    south_region = []
    south_region.extend(south_atlantic + east_south_central + west_south_central)
    
    west_region = []
    west_region.extend(mountain + pacific)

class States:
    _data_ = data._states_data_
    
    def get_state_info(self,full_name):
        """
        Params: 
            full_name: The full name of the state to search. If 'all' is passed, then it will
                        retrieve the full name of all territories.
            
        Returns:
            Dictionary with state information when a state name is passed.
            If 'all' is passed, then it will return the full name of state in list form.
        """
        state_data = self._data_['states']
        
        if full_name == 'all':
            state_info = list(state_data.keys())
            
        else:
            full_name = full_name.title()

            state_info = state_data.get(full_name, 
                        "Sorry try typing the name of the state again, or pass 'all' for full_name to view all states.")
        
        return state_info