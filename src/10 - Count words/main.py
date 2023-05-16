import re
from collections import Counter

def count_words(filename):
  all_words = Counter()

  # Open file for reading
  with open(filename, "r") as file:
    # Iterate line by line
    for line in file:
      # Find all words matching a regex
      words = re.findall(r"[A-Za-z\d']+?\b", line, flags=re.IGNORECASE)
      
      # iterate through words & count it's occurance
      all_words.update(word.upper() for word in words)
  
  # Get the top 20
  filteredWords = all_words.most_common(20)

  print(f"\nTotal Words: {len(all_words)}")
  print("\nTop 20 Words:")
  for word, count in filteredWords:
    print(f"{word.ljust(16)}{count}")
