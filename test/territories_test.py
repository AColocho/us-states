from states import Territories_Abbreviated
from states import Territories_Full_Name
from states import Uninhabited_Territories
from states import Associated_States
from states import Territories
import unittest

class Abbreviated_Test(unittest.TestCase):
    def check_lenght(self):
        """
        Checks there is only 5 territories.
        """
        all_territories = Territories_Abbreviated().all_territories
        self.assertEqual(5,len(all_territories),'There is either less or more than 5 territories recognized.')

class Full_Name_Test(unittest.TestCase):
    def check_lenght(self):
        """
        Checks there is only 5 territories.
        """
        all_territories = Territories_Full_Name().all_territories
        self.assertEqual(5,len(all_territories),'There is either less or more than 5 territories recognized.')

class Uninhabited_Territories_Test(unittest.TestCase):
    def check_lenght(self):
        """
        Checks there is only 7 territories.
        """
        all_territories = Uninhabited_Territories().all_territories
        self.assertEqual(7,len(all_territories),'There is either less or more than 7 territories recognized.')
        
class Associated_States_Test(unittest.TestCase):
    def check_lenght(self):
        """
        Checks there is only 3 territories.
        """
        all_territories = Associated_States().pacific_abbreviated
        self.assertEqual(3,len(all_territories),'There is either less or more than 3 territories recognized.')
        
class Territories_Test(unittest.TestCase):
    def check_search_returns_info(self):
        """
        Checks that the search function returns the correct value.
        """
        PR = Territories().get_territory_info('Puerto Rico')
        full_name = PR['full_name']
        self.assertTrue(full_name == 'Puerto Rico', 'Search function is not retrieving the right value. Used Puerto Rico as a Test.')

if __name__ == "__main__":
    unittest.main()