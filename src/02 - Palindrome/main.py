# Go hang a salami, I’m a lasagna hog.
# gohangasalamiimalasgnahog is a palindrome

def is_palindrome(string):
  sanitizedString = ""
  for char in string.lower():
    if char.isalpha():
      sanitizedString += char
  
  length = len(sanitizedString)
  for i in range(length):
    j = length - i - 1

    lhs = sanitizedString[i]
    rhs = sanitizedString[j]
    
    if lhs != rhs:
      print(False)
      return
  
  print(True)