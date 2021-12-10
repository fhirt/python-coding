import unittest
from money import Bank, Money, Sum


class TestCurrency(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.franc(7) == Money.dollar(7))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(2).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.dollar(5)
        total = five.plus(five)
        reduced = Bank().reduce(total, "USD")
        self.assertEqual(reduced, Money.dollar(10))

    def test_reduce_sum(self):
        expression = Sum(Money.dollar(3), Money.dollar(4))
        result = Bank().reduce(expression, "USD")
        self.assertEqual(result, Money.dollar(7))

    def test_reduce_money(self):
        expression = Money.dollar(5)
        result = Bank().reduce(expression, "USD")
        self.assertEqual(result, Money.dollar(5))

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        total = five.plus(five)
        self.assertEqual(total.addend, five)
        self.assertEqual(total.augend, five)

    def test_exchange_rate(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        dollar = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(dollar, Money.dollar(1))

    def test_identity_rate(self):
        rate = Bank().rate("USD", "USD")
        self.assertEqual(rate, 1)

    def test_mixed_addition(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        expression = Money.dollar(5).plus(Money.franc(10))
        result = bank.reduce(expression, "USD")
        self.assertEqual(result, Money.dollar(10))

    def test_sum_plus_money(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        expression = Sum(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(expression, "USD")
        self.assertEqual(result, Money.dollar(15))

    def test_sum_times(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        expression = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(expression, "USD")
        self.assertEqual(result, Money.dollar(20))

if __name__ == '__main__':
    unittest.main()
