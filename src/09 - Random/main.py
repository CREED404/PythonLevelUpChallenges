from random import randint
from collections import Counter

def roll_dice(*args):
  attempts = 1_000_000
  lowerbound = len(args)
  upperbound = sum(args)
  
  results = Counter()
  for _ in range(attempts):
    roll = (randint(1, arg) for arg in args)
    rollSum = sum(roll)
    
    results[rollSum] += 1
  
  print("OUTCOME PROBABILITY")
  for i in range(lowerbound, upperbound + 1):
    occurances = results[i]
    probability = occurances / attempts * 100
    print(f"{i}\t{probability: .2f}%")