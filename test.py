#!/usr/bin/python3
"""
Python test for parentheses_are_balanced.py
"""

__author__ = 'Ivan Semernyakov'
__date__ = '17.09.2019'

import unittest
from .parentheses_are_balanced import parantheses_are_balanced as pab


class TestPab(unittest.TestCase):
    """
    Test for check balance off brackets
    """

    def test_parentheses_are_balanced(self):
        """
        Test that must return True if parentheses are balanced
        """
        result = pab('[{()}]')
        self.assertTrue(result)

    def test_parentheses_are_not_balanced(self):
        """
        Test that must return False if parentheses are no balanced
        """
        result = pab('[{()')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()