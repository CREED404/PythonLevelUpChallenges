import time
import random

def waiting_game():
    timeToWait = random.randint(2, 4)
    input(f"You target time is {timeToWait} seconds\n----Press Enter to Begin----")
    ima = time.time()
    input(f"Press Enter Again after {timeToWait} seconds...")
    elapsed=time.time()-ima
    if (elapsed-timeToWait) == 0:
        satatus = "You were so Good!"
    elif (elapsed-timeToWait) > 0:
        satatus = "too slow"
    else:
        satatus = "too fast"
    print(f"Elapsed time: {elapsed:.3f} seconds ({(elapsed-timeToWait):.3f} seconds {satatus})")
