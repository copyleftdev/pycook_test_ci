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



if __name__ == '__main__':
  unittest.main()