def sort_words(string):
  words = string.split()
  result = sorted(words, key=str.casefold)
  return " ".join(result)

# Observations
#
# `str.casefold` builds over `str.lower` to be locale independent