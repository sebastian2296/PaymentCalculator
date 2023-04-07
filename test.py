import unittest
from src.payment_calculator import PaymentCalculator 
from src.rate import Rate
from src.shift import Shift

class TestPaymentCalculator(unittest.TestCase):

    def setUp(self):
        rates = [
            Rate('MO', 0, 9, 25),
            Rate('MO', 9, 18, 15),
            Rate('MO', 18, 24, 20),
            Rate('TU', 0, 9, 25),
            Rate('TU', 9, 18, 15),
            Rate('TU', 18, 24, 20),
            Rate('WE', 0, 9, 25),
            Rate('WE', 9, 18, 15),
            Rate('WE', 18, 24, 20),
            Rate('TH', 0, 9, 25),
            Rate('TH', 9, 18, 15),
            Rate('TH', 18, 24, 20),
            Rate('FR', 0, 9, 25),
            Rate('FR', 9, 18, 15),
            Rate('FR', 18, 24, 20),
            Rate('SA', 0, 9, 30),
            Rate('SA', 9, 18, 20),
            Rate('SA', 18, 24, 25),
            Rate('SU', 0, 9, 30),
            Rate('SU', 9, 18, 20),
            Rate('SU', 9, 18, 20)
        ]
        self.calculator = PaymentCalculator(rates)

    def test_calculate_shift_payment(self):
        shift = Shift('MO', '07:00', '10:00')
        expected_payment = 25 * 2 + 15
        self.assertEqual(self.calculator.calculate_shift_payment(shift), expected_payment)

if __name__ == '__main__':
    unittest.main()