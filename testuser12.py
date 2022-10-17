import unittest
import userstory12

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertTrue(userstory12.parentsNotTooOld is not 0)
    def test2(self):
        self.assertFalse(userstory12.parentsNotTooOld is 0 )


unittest.main()

