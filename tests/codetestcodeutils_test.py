#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from app.codetestcodeutils import codetestcodeutils
from collections import OrderedDict



class TestCodeTestSuite(unittest.TestCase):

  def test_unpack_seq_to_sperate_vars(self):
    tv = codetestcodeutils()
    self.assertEqual(tv.unpack_seq_to_seperate_vars(),(1, 2, 1, 2, 3, "Don Johnson", (6, 23, 1795),"Pasadena", "h", "e", "l", "l", "o"))

  def test_keeping_last_n_items(self):
    tv = codetestcodeutils()
    with open('tests/data/sample.txt') as f:
      for line, prevlines, in  tv.keep_last_n_items(f,'test',5):
        for pline in prevlines:
          self.assertEqual(12,len(pline))

  def test_find_smallest_n_items(self):
    tv = codetestcodeutils()
    portfolio = [
      {'name':'IBM', 'shares':100, 'price':91.1},
      {'name':'APPL', 'shares':50, 'price':543.22},
      {'name':'IBM', 'shares':200, 'price':21.09},
      {'name':'IBM', 'shares':35, 'price':31.75},
      {'name':'IBM', 'shares':45, 'price':16.35},
      {'name':'ACME', 'shares':75, 'price':115.65}
    ]

    self.assertEqual(tv.find_smallest_n_items(3,portfolio,"price"), [{'price': 16.35, 'name': 'IBM', 'shares': 45}, {'price': 21.09, 'name': 'IBM', 'shares': 200}, {'price': 31.75, 'name': 'IBM', 'shares': 35}])

  def test_find_largest_n_items(self):
     tv = codetestcodeutils()
     portfolio = [
      {'name':'IBM', 'shares':100, 'price':91.1},
      {'name':'APPL', 'shares':50, 'price':543.22},
      {'name':'IBM', 'shares':200, 'price':21.09},
      {'name':'IBM', 'shares':35, 'price':31.75},
      {'name':'IBM', 'shares':45, 'price':16.35},
      {'name':'ACME', 'shares':75, 'price':115.65}
    ]
     self.assertEqual(tv.find_largest_n_items(3,portfolio,"price"),[{'price': 543.22, 'name': 'APPL', 'shares': 50}, {'price': 115.65, 'name': 'ACME', 'shares': 75}, {'price': 91.1, 'name': 'IBM', 'shares': 100}])
  def test_map_to_multiple_values(self):
    tv = codetestcodeutils()
    test_list = list(range(0,20))
    assert_vector =  {'vector_a': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}
    self.assertEqual(tv.map_keys_to_mutiple_values('temp','vector_a',test_list),assert_vector)

  def test_dict_in_order(self):
    tv = codetestcodeutils()
    test_dict = {'vector1':1,'vector2':2,'vector3':3}
    assert_vector = tv.keep_dict_in_order(test_dict)
    self.assertEqual(OrderedDict(),assert_vector)

  def test_calculate_dict_min(self):
    prices = {'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
    tv = codetestcodeutils()
    assert_vector = (10.75, 'FB')
    self.assertEqual(tv.calculate_dict_min(prices),assert_vector)

  def test_calculate_dict_max(self):
    prices = {'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
    tv = codetestcodeutils()
    assert_vector = (612.78, 'AAPL')
    self.assertEqual(tv.calculate_dict_max(prices),assert_vector)

  def test_find_dict_keys_in_common(self):
    a = {'x':1, 'y':2, 'z':3}
    b = {'w':10, 'x':11, 'y':2}
    tv = codetestcodeutils()
    av = ['y', 'x', 'w']
    self.assertEqual(tv.find_dict_keys_in_common(a, b),av)

  def test_find_key_value_in_common(self):
    a = {'x':1, 'y':2, 'z':3}
    b = {'w':10, 'x':11, 'y':2}
    tv = codetestcodeutils()
    av = [('y', 2), ('x', 11), ('w', 10)]
    self.assertEqual(tv.find_key_values_in_common(a,b),av)




if __name__ == '__main__':
  unittest.main()
