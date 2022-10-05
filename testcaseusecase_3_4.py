import unittest
import Userstory3
import userstory4

class TestStringMethods(unittest.TestCase):
	
    def test1(self):
        self.assertTrue(len(Userstory3.individualList()) is not 0)
    
    def test5(self):
        self.assertFalse(len(userstory4.familyList()) is 0)
		
	
		

unittest.main()