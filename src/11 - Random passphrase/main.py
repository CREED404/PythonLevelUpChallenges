from random import randint
import secrets

def generate_passphrase(count):
  with open("diceware.wordlist.asc", "r") as file:
    lines = file.readlines()[2:7778]
    all_words = [line.split()[1] for line in lines]

  keys = [secrets.choice(all_words) for _ in range(count)]
  return ' '.join(keys)