def island_count(grid):
    count = 0
    visited = set()
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if _explore_dfs(grid, r, c, visited) == True:
                count += 1
    return count

def _explore_dfs(grid, r, c, visited):
    # Base cases
    if r < 0 or r == len(grid) or c < 0 or c == len(grid[0]):
        return False

    if grid[r][c] == "W":
        return False
    
    if (r, c) in visited:
        return False
    else:
        visited.add((r, c))
    
    if grid[r][c] == "W":
        return False
    
    # Recursive calls
    neighbors = [
        (r+1, c),
        (r, c+1),
        (r-1, c),
        (r, c-1)
    ]
    for neighbor in neighbors:
        r, c = neighbor
        if _explore_dfs(grid, r, c, visited) == False:
            continue
    return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
print(island_count(grid)) # -> 3