import unittest
import userstory16

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertTrue(userstory16.maleLastNames is not 0)
unittest.main()