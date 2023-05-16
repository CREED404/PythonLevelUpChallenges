import re
from collections import Counter

def count_words(filename):
  # Open file for reading
  with open(filename, "r") as file:
    # Find all words matching a regex
    all_words = re.findall(r"[A-Za-z\d']+?\b", file.read())
    print(f"\nTotal Words: {len(all_words)}")
    
    word_counts = Counter(all_words)
  
    # Get the top 20
    filteredWords = word_counts.most_common(20)
    print("\nTop 20 Words:")
    for word, count in filteredWords:
      print(f"{word.upper().ljust(16)}{count}")
