#!/usr/bin/env python
# Author: Rebecca Li
# Date: 9-11-2014
from numpy import array   # Import array from package numpy
numbers= [43, 47, 72, 53, 59, 88, 61, 102, 7, 83, 87, 203, 89, 95, 97, 101, 2, 10, 102,
          3, 98, 5, 11, 32, 13, 17, 46, 19, 23, 27, 90, 29, 31, 35, 100, 37, 41, 56, 67,
          120, 71, 73, 303, 79]       # Create a list of numbers, type:int
numbers = array(numbers,int)         # Change the list into an array                       
total = sum(numbers)                  # Use built-in function sum to obtain the sum of numbers

print 'The sum of given numbers is %s' %total                       # Print out the sum
