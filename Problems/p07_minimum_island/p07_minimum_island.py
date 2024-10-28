def minimum_island(grid):
    count = 0
    visited = set()
    min_size = float("inf")
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            curr_size = _explore_dfs(grid, r, c, visited)
            if curr_size > 0:
                min_size = min(min_size, curr_size)
    return min_size

def _explore_dfs(grid, r, c, visited):
    # Base cases
    if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]):
        return 0

    if grid[r][c] == "W":
        return 0
    
    if (r, c) in visited:
        return 0
    else:
        visited.add((r, c))
    
    # Recursive calls
    neighbors = [
        (r+1, c),
        (r, c+1),
        (r-1, c),
        (r, c-1)
    ]
    size = 1
    for neighbor in neighbors:
        r, c = neighbor
        size += _explore_dfs(grid, r, c, visited)
    return size

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
print(minimum_island(grid)) # -> 2