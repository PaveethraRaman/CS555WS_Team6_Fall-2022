import unittest
import userstory17

class TestNoMarriedDescendents(unittest.TestCase):
    def testcase1(self):
        self.assertFalse(userstory17.NoMarriagesToDescendents ==  0)

unittest.main()