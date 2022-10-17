import unittest
import userstory10

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertTrue(userstory10.marriageAfter14 is not 0)
unittest.main()