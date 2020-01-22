#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from kata_1 import StringCalculator


class AddTestCase(unittest.TestCase):
    """
    Class test for the Add method
    """

    test_values = (
    ('', 0), ('1', 1), ('1,2', 3), ('1\n2,3', 6), ('//;\n2;3', 5), ('//[***]\n2***3***1001', 5),
    ('//[%%][*]\n2%%3*1', 6), ('//;\n2;3;1001', 5))

    def test_sum(self):
        """
        Test referenced values
        :return:
        """
        test_method = StringCalculator()
        for value, expected in self.test_values:
            self.assertEqual(expected, test_method.add(value))
        print test_method.GetCalledCount()


if __name__ == '__main__':
    unittest.main()
