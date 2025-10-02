import unittest
from IncrementFunction import increment
class TestFunction(unittest.TestCase):
    
    def test_Increment(self):
        self.assertEqual(increment(5), 6)
        self.assertEqual(increment(-8), -7)
        self.assertEqual(increment(0), 1)

if __name__ == '__main__':
    unittest.main()

