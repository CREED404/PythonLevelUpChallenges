from random import randint
from datetime import datetime

def waiting_game():
  duration = randint(2,4)
  print(f"Your target time is {duration} seconds")

  hasStarted = False

  while True:
    startMessage = "---Press Enter to Begin---"
    endMessage = f"...Press Enter again after {duration} seconds..."
    message = startMessage if not hasStarted else endMessage
    
    userInput = input(message)

    if userInput == '':
      if hasStarted:
        endDate = datetime.now()
        elapsedDelta = endDate - startDate

        seconds = elapsedDelta.seconds + elapsedDelta.microseconds / 1_000_000
        print(f"Elapsed time: {seconds: .3f} seconds")

        if duration == seconds:
          print("(Unbelievable! Perfect timing!)")
        elif duration < seconds:
          print(f"({seconds - duration: .3f} seconds too slow)")
        else:
          print(f"({duration - seconds: .3f} seconds too fast)")
        return
      else:
        hasStarted = True
        startDate = datetime.now()
