from pprint import pprint

def solve_sudoku(puzzle):
  print("INPUT:")
  pprint(puzzle)

  # Find missing indices
  missing_indices = []
  for i, array in enumerate(puzzle):
    for j, el in enumerate(array):
      if el == 0:
        missing = (i, j)
        missing_indices.append(missing)

  options = set(range(1,10))

  i = 0
  while len(missing_indices) > 0:
    (x, y) = missing_indices[i]
    
    known = set()
    horizontal = puzzle[x]
    vertical = [line[y] for line in puzzle]
    
    box = []
    box_lower_v = (x // 3) * 3
    box_higher_v = box_lower_v + 3
    box_lower_h = (y // 3) * 3
    box_higher_h = box_lower_h + 3
    for box_y in range(box_lower_v, box_higher_v):
      box += puzzle[box_y][box_lower_h:box_higher_h]

    known.update(horizontal)
    known.update(vertical)
    known.update(box)
    known.remove(0)

    unknown = known.symmetric_difference(options)

    found = len(unknown) == 1
    if found:
      puzzle[x][y] = unknown.pop()
      missing_indices.pop(i)
      i = 0 if i >= len(missing_indices) else i
    else:
      i = (i + 1) % len(missing_indices)
  
  print("OUTPUT:")
  pprint(puzzle)
