"""
This module contains unit tests for variance and standard deviation functions.

The tests cover typical values, non-integer values.
"""

from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt


class StatisticsTest(TestCase):
    """Test cases for variance and standard deviation functions."""

    def test_average_typical_values(self):
        """Test average of typical values."""
        self.assertEqual(3.0, average([1, 2, 3, 4, 5]))
        self.assertEqual(5.0, average([5, 5, 5, 5, 5]))
        self.assertEqual(3.5, average([1, 2, 3, 4, 5, 6]))

    def test_average_single_value(self):
        """Test average with a single value."""
        self.assertEqual(6.9, average([6.9]))

    def test_average_empty_list(self):
        """Test that average raises ValueError on empty list."""
        with self.assertRaises(ValueError):
            average([])

    def test_variance_empty_list(self):
        with self.assertRaises(ValueError):
            variance([])

    def test_variance_typical_values(self):
        """Test variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """Test variance with decimal values."""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_stdev(self):
        """Test standard deviation calculation."""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=1)
