from random import randint
import re

def _random_key(lower=1, upper=6):
  return ''.join(str(randint(lower,upper)) for _ in range(5))

def generate_passphrase(count):
  with open("diceware.wordlist.asc", "r") as file:
    diceware_pair = {}
    for found in re.findall(r"\d{5}\s+.+", file.read()):
      pair = found.split("\t")
      diceware_pair[pair[0]] = pair[1]

  keys = [diceware_pair[f"{random_key()}"] for _ in range(count)]
  return ' '.join(keys)