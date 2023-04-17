"""
    Sample tests
"""


from app import calc
from django.test import SimpleTestCase


class ClacTests(SimpleTestCase):
    """

    Args:
        SimpleTestCase for testing calc module
    """

    def test_added_numbers(self):
        """AI is creating summary for test_added_numbers
        """
        res = calc.add_numbers(9,41)

        self.assertEqual(res, 50)

    def test_subtract_numbers(self):
        """ Subtracting"""
        res = calc.subtract(23,18)

        self.assertEqual(res, 9)