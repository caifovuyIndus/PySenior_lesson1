import unittest
from main import *

class MainTest(unittest.TestCase):
    def test_sumv_value(self):
        self.assertEqual(sum_value(2, 3), 6)

if __name__ =='__main__':
    unittest.main()