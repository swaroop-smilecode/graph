from collections import deque

def closest_carrot(grid, starting_row, starting_col):
    # This is undirected graph, hence you need "visited" set.
    # If there are more than one value need to be kept inside the 
    # set, then keep them as list of tuples.
    visited = set([(starting_row, starting_col)])
    # From the given cell, explore the grid using BFS algo. The reason
    # to choose BFS algo is, it explores in all directions evenly.
    # When we do such kind of exploration, we can say that the first carrot
    # we reach is the nearest carrot.

    # The momemnt you thought of BFS, immediatly queue should come into your mind.
    queue = deque([(starting_row, starting_col, 0)])

    # let's start the BFS work
    # BFS means --> Queue 
    # Queue means --> popleft & append
    while queue:
        row, col, distance = queue.popleft()

        # If the cell currently you are on is carrot? Then you found the target.
        # Just return whatever has been calculated by BFS as of now. In this case
        # it's distance, hence return distance.

        # DFS means --> Recursion 
        # Recuriosn means --> Base case is your first step in the DFS fn.
        # Similarly
        # BFS means --> While loop
        # While loop means --> Exit condition is your first step & Exit condition is 
        # nothing but finding the target.
        if grid[row][col] == "C":
            return distance

        # Let's start the actual BFS work
        deltas = [(1,0),(-1,0),(0,1),(0,-1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            pos = (neighbor_row, neighbor_col)
            if (neighbor_row < 0 or neighbor_row == len(grid) or
                neighbor_col < 0 or neighbor_col == len(grid[0]) or
                grid[neighbor_row][neighbor_col] == "X" or
                pos in visited):
                continue
            else:
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))
    return -1

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

closest_carrot(grid, 1, 2) # -> 4