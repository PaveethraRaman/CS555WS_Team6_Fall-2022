import unittest
import userstory22

class TestUserUniqueIDS(unittest.TestCase):
    def testcase1(self):
        self.assertFalse(userstory22.UniqueIDS == 0)

unittest.main()