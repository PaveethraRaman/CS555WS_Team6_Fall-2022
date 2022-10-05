import unittest
import user6
import USER5

class Testing(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(user6.MarriageBeforeDeath, 0)

    def test2(self):
        self.assertIsNone(USER5.getDeathDate, msg=None)


unittest.main()