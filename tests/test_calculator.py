import unittest

from calculator import add, subtract, multiply, divide, reminder_del


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_reminder_of_division_null(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_reminder_of_division(self):
        self.assertEqual(reminder_del(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
