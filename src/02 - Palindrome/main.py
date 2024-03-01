# Go hang a salami, I’m a lasagna hog.
# gohangasalamiimalasgnahog is a palindrome

def isPalindrome(string: str):
    string = "".join([x for x in string.lower() if x.isalpha()])
    return string == "".join([string[i] for i in reversed(range(len(string)))])
