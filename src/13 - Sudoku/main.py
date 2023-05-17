from collections import deque

def print_sudoku(puzzle):
  for i, line in enumerate(puzzle):
    formatted = []
    for j, el in enumerate(line):
      formatted.append("*" if el == 0 else str(el))
      if j in [2,5]:
        formatted.append("|")
    print('  '.join(formatted))
    if i in [2,5]:
      print("-" * 31)

def solve_sudoku(puzzle):
  print("INPUT:")
  print_sudoku(puzzle)

  # Using double-ended queue for cheaper cost of rotate/pop operation of just 1 element compared
  # to list when removing an element from the middle which would cost shifting subsequent elements
  missing_indices = deque((i, j) for i, array in enumerate(puzzle) for j, el in enumerate(array) if el == 0)

  while missing_indices:
    (x, y) = missing_indices[0]
    
    horizontal = set(puzzle[x])
    vertical = {line[y] for line in puzzle}
    
    box_y1 = (x // 3) * 3
    box_y2 = box_y1 + 3
    box_x1 = (y // 3) * 3
    box_x2 = box_x1 + 3
    box = {puzzle[box_y][box_x] for box_y in range(box_y1, box_y2) for box_x in range(box_x1, box_x2)}

    known = horizontal | vertical | box
    known.remove(0)

    unknown = set(range(1,10)) - known

    found = len(unknown) == 1
    if found:
      puzzle[x][y] = unknown.pop()
      missing_indices.popleft()
    else:
      missing_indices.rotate(-1)
  
  print("OUTPUT:")
  print_sudoku(puzzle)
