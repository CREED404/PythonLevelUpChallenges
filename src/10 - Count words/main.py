import re
from collections import Counter

def count_words(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        content=f.read()
    count = Counter()
    words_count = 0
    for word in re.findall(r"[A-Za-z\d']+?\b", file.read()):
        count[word.lower()] += 1
        words_count += 1
    print(f"Total words: {words_count}")
    #print(list(count.keys()))
    for w, c in list(sorted(count.items(), key=lambda x: x[1], reverse=True))[:20]:
        print(f"{w}: {c}")
