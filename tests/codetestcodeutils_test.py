#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from app.codetestcodeutils import codetestcodeutils



class TestCodeTestSuite(unittest.TestCase):

  def test_unpack_seq_to_sperate_vars(self):
    test_vector = codetestcodeutils()
    self.assertEqual(test_vector.unpack_seq_to_seperate_vars(),(1, 2, 1, 2, 3, "Don Johnson", (6, 23, 1795),"Pasadena", "h", "e", "l", "l", "o"))

  def test_keeping_last_n_items(self):
    test_vector = codetestcodeutils()
    with open('tests/data/sample.txt') as f:
      for line, prevlines, in  test_vector.keep_last_n_items(f,'test',5):
        for pline in prevlines:
          self.assertEqual(12,len(pline))

  def test_find_smallest_n_items(self):
    test_vector = codetestcodeutils()
    portfolio = [
      {'name':'IBM', 'shares':100, 'price':91.1},
      {'name':'APPL', 'shares':50, 'price':543.22},
      {'name':'IBM', 'shares':200, 'price':21.09},
      {'name':'IBM', 'shares':35, 'price':31.75},
      {'name':'IBM', 'shares':45, 'price':16.35},
      {'name':'ACME', 'shares':75, 'price':115.65}
    ]

    self.assertEqual(test_vector.find_smallest_n_items(3,portfolio,"price"), [{'price': 16.35, 'name': 'IBM', 'shares': 45}, {'price': 21.09, 'name': 'IBM', 'shares': 200}, {'price': 31.75, 'name': 'IBM', 'shares': 35}])

  def test_find_largest_n_items(self):
     test_vector = codetestcodeutils()
     portfolio = [
      {'name':'IBM', 'shares':100, 'price':91.1},
      {'name':'APPL', 'shares':50, 'price':543.22},
      {'name':'IBM', 'shares':200, 'price':21.09},
      {'name':'IBM', 'shares':35, 'price':31.75},
      {'name':'IBM', 'shares':45, 'price':16.35},
      {'name':'ACME', 'shares':75, 'price':115.65}
    ]
     self.assertEqual(test_vector.find_largest_n_items(3,portfolio,"price"),[{'price': 543.22, 'name': 'APPL', 'shares': 50}, {'price': 115.65, 'name': 'ACME', 'shares': 75}, {'price': 91.1, 'name': 'IBM', 'shares': 100}])





if __name__ == '__main__':
  unittest.main()