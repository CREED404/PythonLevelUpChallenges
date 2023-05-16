import re

def count_words(filename):
  all_words = {}

  # Open file for reading
  with open(filename, "r") as file:
    # Iterate line by line
    for line in file:
      # Find all words matching a regex
      words = re.findall(r"[A-Za-z\d']+?\b", line, flags=re.IGNORECASE)
      
      # iterate through words & count it's occurance
      for word in words:
        word = word.upper()
        all_words.setdefault(word, 0)
        all_words[word] += 1
  
  # Sort the dictionary {words:count} based on  the count
  sortedDict = dict(sorted(all_words.items(), key=lambda x: x[1], reverse=True))
  
  # Convert sorted dictionary to list & slice the top 20
  filteredWords = list(sortedDict.items())[:20]

  print(f"\nTotal Words: {len(all_words)}")
  print("\nTop 20 Words:")
  for word in filteredWords:
    print(f"{word[0].ljust(16)}{word[1]}")
