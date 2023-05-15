import random

def roll_dice(*args):
  attempts = 1_000_000
  lowerbound = len(args)
  upperbound = sum(args)
  
  results = {}
  for i in range(attempts):
    rollSum = 0
    for arg in args:
      rollSum += random.randint(1, arg)
    
    results.setdefault(rollSum, 0)
    results[rollSum] += 1
  
  print("OUTCOME PROBABILITY")
  for i in range(lowerbound, upperbound + 1):
    occurances = results.get(i, 0)
    probability = occurances / attempts * 100
    print(f"{i}\t{probability: .2f}%")