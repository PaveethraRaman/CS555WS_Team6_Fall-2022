import unittest
import userstory18

class TestNoMarriedSiblings(unittest.TestCase):
    def testcase1(self):
        self.assertFalse(userstory18.SiblingsNotMarry == 0)

unittest.main()