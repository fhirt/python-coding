import unittest
from currency import Dollar


class TestCurrency(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(product.amount, 10)
        product = five.times(3)
        self.assertEqual(product.amount, 15)
        
    def test_equality(self):
        self.assertTrue(Dollar(5)==Dollar(5))
        self.assertFalse(Dollar(5)==Dollar(6))

    
if __name__ == '__main__':
    unittest.main()