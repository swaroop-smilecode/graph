def closest_carrot(grid, starting_row, starting_col):
    visited = set()
    minimum = float("inf")
    return _explore_bfs(grid, starting_row, starting_col, 0, visited)

from collections import deque
def _explore_bfs(grid, starting_row, starting_col, distance, visited):
    queue = deque([(starting_row, starting_col, distance)])

    while queue:
        starting_row, starting_col, distance = queue.popleft()
        # Base case
        if starting_row < 0 or starting_row == len(grid) \
            or starting_col < 0 or starting_col == len(grid[0]):
            continue
        if grid[starting_row][starting_col] == "C":
            return distance
        if grid[starting_row][starting_col] == "X":
            continue
        if (starting_row, starting_col) in visited:
            continue
        else:
            visited.add((starting_row, starting_col))

        # Recursive calls
        neighbors = [(starting_row+1, starting_col), 
                     (starting_row-1, starting_col), 
                     (starting_row, starting_col+1), 
                     (starting_row, starting_col-1)
                    ]
        for neighbor in neighbors:
            r, c = neighbor
            queue.append((r, c, distance+1))
    return -1

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]
print(closest_carrot(grid, 1, 2)) # -> 4