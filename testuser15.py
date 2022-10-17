import unittest
import userstory15

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(userstory15.lessThan15Siblings , 0)
unittest.main()
