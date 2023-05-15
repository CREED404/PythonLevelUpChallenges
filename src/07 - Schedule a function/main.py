import time

def schedule_function(timestamp, function, message):
  startTime = time.time()
  duration = round(timestamp - startTime)

  while duration > 0:
    duration -= 1
    time.sleep(1)
  
  function(message)