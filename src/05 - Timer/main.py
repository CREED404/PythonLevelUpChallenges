from random import randint
import time

def waiting_game():
  duration = randint(2,4)
  print(f"Your target time is {duration} seconds")

  input("---Press Enter to Begin---")
  start = time.perf_counter()

  input(f"...Press Enter again after {duration} seconds...")
  elapsed = time.perf_counter() - start

  print(f"Elapsed time: {elapsed: .3f} seconds")
  if duration == elapsed:
    print("(Unbelievable! Perfect timing!)")
  elif duration < elapsed:
    print(f"({elapsed - duration: .3f} seconds too slow)")
  else:
    print(f"({duration - elapsed: .3f} seconds too fast)")
