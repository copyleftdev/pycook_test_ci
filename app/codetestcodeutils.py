#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque, OrderedDict, Counter
import heapq



class codetestcodeutils(object):

  def unpack_seq_to_seperate_vars(self):
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

    previous_lines = deque(maxlen=history)
    for line in  lines:
      if patterns in line:
        yield line, previous_lines
      previous_lines.append(line)


  def find_largest_n_items(self,limit, data_series,value_vector):

    largest_value = heapq.nlargest(limit ,data_series, key=lambda s: s[value_vector])
    return largest_value

  def find_smallest_n_items(self, limit, data_series,value_vector):

    smallest_value = heapq.nsmallest(limit, data_series, key=lambda s: s[value_vector])
    return smallest_value


  def map_keys_to_mutiple_values(self,dict_name, key_name, values):

    dict_name = {
      key_name : []
    }
    for value in values:
      dict_name[key_name].append(value)
    return dict_name

  def keep_dict_in_order(self,dict_name):
    dict_name = OrderedDict()
    return dict_name

  def calculate_dict_min(self, dict_name):
    result = min(zip(dict_name.values(),dict_name.keys()))
    return result

  def calculate_dict_max(self, dict_name):
    result = max(zip(dict_name.values(),dict_name.keys()))
    return result

  def find_dict_keys_in_common(self, dict_one, dict_two):
    result = dict_one.keys() and dict_two.keys()
    return result

  def find_key_values_in_common(self, dict_one,dict_two):
    result =  dict_one.items() and dict_two.items()
    return result

  def remove_dupes_from_seq_with_order(self, seq_name):
    seen = set()
    for item in seq_name:
      if item not in seen:
        yield item
        seen.add(item)

  def find_most_occuring_item_in_seq(self, seq_name,top_count):
    word_counts = Counter(seq_name)
    return word_counts.most_common(top_count)

  def sort_dicts_by_common_keys(self, dict_name, sort_vector):
    sorted_dict =  sorted(dict_name, key=lambda r: r[sort_vector])
    return sorted_dict

  def calc_sum_of_square(self,list_name):
    s = sum( x * x for x in list_name)
    return s

  def reduce_across_fields_in_data_structure(self,sname,fname):
    min_sum = min(s['{}'.format(fname)] for s in sname)
    return min_sum
