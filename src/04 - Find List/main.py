# input          : [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# find 2         : [[0, 0, 1], [0, 1], [1, 1]]
# find [1, 2, 3] : [[0, 0], [1]]

def index_all(array, pattern):
  result = []

  for i, el in enumerate(array):
    if el == pattern:
      result.append([i])
    elif isinstance(el, list):
      for j in index_all(el, pattern):
        result.append([i] + j)

  return result