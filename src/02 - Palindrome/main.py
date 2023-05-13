# Go hang a salami, I’m a lasagna hog.
# gohangasalamiimalasgnahog is a palindrome

def is_palindrome(string):
  i = 0
  j = len(string) - 1

  while i < j:
    lhs = string[i]
    rhs = string[j]

    if not lhs.isalpha():
      i += 1
      continue

    if not rhs.isalpha():
      j -= 1
      continue

    if lhs.lower() != rhs.lower():
      return False

    i += 1
    j -= 1
  
  return True