# Go hang a salami, I’m a lasagna hog.
# gohangasalamiimalasgnahog is a palindrome

import re

def is_palindrome(string):
  lhs = ''.join(re.findall(r'[a-z]', string.lower()))
  rhs = lhs[::-1]
  return lhs == rhs