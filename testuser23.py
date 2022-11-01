import unittest
import userstory23

class TestUserUniqueIDS(unittest.TestCase):
    def testcase1(self):
        self.assertFalse(userstory23.UniqueNameAndBirthDate == 0)

unittest.main()