import unittest
import numpy as np
from duration_calculator import durationCalculator
class TestFunction(unittest.TestCase):
    
    def test_calculator(self):
        self.assertEqual(durationCalculator(str(np.datetime64('today') - np.timedelta64(6, 'D'))), "6 days")
        self.assertEqual(durationCalculator(str(np.datetime64('today') - np.timedelta64(19, 'D'))), "19 days")

if __name__ == '__main__':
    unittest.main()