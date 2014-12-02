#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque

class codetestcodeutils(object):

  def unpack_seq_to_seperate_vars(self):
    '''
          1.1. Unpacking a Sequence into Separate Variables
          Problem
          -----------------------
          You have an N-element tuple or sequence that you would like to
          unpack into a collection of N variables.
          Solution
          -----------------------
          Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.
          The only requirement is that the number of variables and structure match the sequence. For example:
    '''

    a = (1, 2)
    data_flat = [1, 2, 3]
    data_nested  = ["Don Johnson",(6,23,1795),"Pasadena"]
    x,y = a
    hello = "hello"
    one, two, three = data_flat
    name, date_of_birth, location = data_nested
    w,o,r,l,d = hello

    return(x,y,one,two,three, name, date_of_birth,location,w,o,r,l,d)

  def keep_last_n_items(self, lines, patterns,history=5):
    '''
          1.3. Keeping the Last N Items
          Problem
          ----------
            You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.
          Solution
          -----------
            Keeping a limited history is a perfect use for a collections.deque. For example, the following code performs a simple text match on a sequence of lines and yields the matching line along with the previous N lines of context when found:
    '''
    previous_lines = deque(maxlen=history)
    for line in  lines:
      if patterns in line:
        yield line, previous_lines
      previous_lines.append(line)
