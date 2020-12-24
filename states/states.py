class States_Abbreviated:
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