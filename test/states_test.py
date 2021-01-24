from states import States_Abbreviated
from states import States_Full_Name
from states import States
import unittest

class Abbreviated_Test(unittest.TestCase):
    def check_DC_has_statehood(self):
        """
        This test checks to see if DC is consider a state when it should be.
        """
        DC_state = States_Abbreviated(True)
        DC = set(DC_state.all_states + DC_state.south_atlantic + DC_state.south_region)
        
        self.assertTrue('DC' in DC, 'DC is not consider a state when it should be.')
    
    def check_DC_not_statehood(self):
        """
        This test checks to see if DC is consider a state when it should not be.
        """
        DC_not_state = States_Abbreviated(False)
        not_DC = set(DC_not_state.all_states + DC_not_state.south_atlantic + DC_not_state.south_region)
        self.assertFalse('DC' in not_DC, 'DC is consider a state when it should not be.')
    
    def check_50_states(self):
        """
        Checks that a length of 50 is returned with all_states. This does not include DC.
        """
        states = States_Abbreviated(False)
        all_states = states.all_states
        self.assertEqual(50, len(all_states), 'There is either less or more than 50 states recognized.')
        
    def check_51_states(self):
        """
        Checks that a length of 51 is return with all_states. This includes DC.
        """
        states = States_Abbreviated(True)
        all_states = states.all_states
        self.assertEqual(51, len(all_states, 'There is less or more than 51 states recognized. This includes DC.'))

class States_Full_Name_Test(unittest.TestCase):
    def check_DC_has_statehood(self):
        """
        This test checks to see if DC is consider a state when it should be.
        """
        DC_state = States_Full_Name(True)
        DC = set(DC_state.all_states + DC_state.south_atlantic + DC_state.south_region)
        
        self.assertTrue('District of Columbia' in DC, 'District of Columbia is not consider a state when it should be.')
    
    def check_DC_not_statehood(self):
        """
        This test checks to see if DC is consider a state when it should not be.
        """
        DC_not_state = States_Full_Name(False)
        not_DC = set(DC_not_state.all_states + DC_not_state.south_atlantic + DC_not_state.south_region)
        self.assertFalse('District of Columbia' in not_DC, 'District of Columbia is consider a state when it should not be.')
    
    def check_50_states(self):
        """
        Checks that a length of 50 is returned with all_states. This does not include District of Columbia.
        """
        states = States_Full_Name(False)
        all_states = states.all_states
        self.assertEqual(50, len(all_states), 'There is either less or more than 50 states recognized.')
        
    def check_51_states(self):
        """
        Checks that a length of 51 is return with all_states. This includes District of Columbia.
        """
        states = States_Full_Name(True)
        all_states = states.all_states
        self.assertEqual(51, len(all_states, 'There is less or more than 51 states recognized. This includes District of Columbia.'))
        
class State_Test(unittest.TestCase):
    def check_search_returns_info(self):
        """
        Checks that the search function returns the correct value.
        """
        VA = States().get_state_info('Virginia')
        full_name = VA['full_name']
        self.assertTrue(full_name == 'Virginia', 'Search function is not retrieving the right value. Used Virginia as a Test.')

if __name__ == "__main__":
    unittest.main()