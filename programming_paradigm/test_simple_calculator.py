import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(1, -1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
    
    def test_subtract(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(1, -1), 2)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(0, 0), 0)

    def test_multiply(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.multiply(1, 2), 2)
        self.assertEqual(calculator.multiply(1, -1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)
        self.assertEqual(calculator.multiply(0, 0), 0)

    def test_divide(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.divide(1, 2), 0.5)
        self.assertEqual(calculator.divide(1, -1), -1)
        self.assertEqual(calculator.divide(-1, -1), 1)
        self.assertEqual(calculator.divide(0, 1), 0)
        self.assertEqual(calculator.divide(1, 0), "Error: Cannot divide by zero.")
        self.assertEqual(calculator.divide(1, "a"), "Error: Please enter numeric values only.")