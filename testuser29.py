import unittest
import userstory29

class TestListDeceased(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(userstory29.DeceasedIndividuals != 0)

unittest.main()