def best_bridge(grid):
    first_island = None
    flag = False
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == "L":
                potential_island = _explore_dfs(grid, row, col, set())
                if len(potential_island) > 0:
                    first_island = potential_island
                    flag = True
                    break
        if flag == True:
            break
    # Sometimes, we append only first node into queue. That's becasue we 
    # Initiate BFS only on first node & that continues acorss the problem.
    # But, here we need to initiate BFS on each cell of the first_island.
    # That's why will push indexes of every cell into the queue & obviously 
    # the starting distance is 0.
    from collections import deque
    queue = deque([])
    for cell in first_island:
        row, col = cell
        queue.append((row, col, 0))

    visited = set()
    while queue:
        row, col, distance = queue.popleft()
        # Base case
        if row < 0 or row == len(grid):
            continue
        if col < 0 or col == len(grid[0]):
            continue

        if grid[row][col] == "L" and (row, col) not in first_island:
            return distance - 1

        if (row, col) in visited:
            continue
        else:
            visited.add((row, col))
        # Recursive calls
        neighbors = [
            (row+1, col),
            (row-1, col),
            (row, col+1),
            (row, col-1)
        ]
        for neighbor in neighbors:
            row, col = neighbor
            queue.append((row, col, distance+1))
    # We need to return distance-1, because the moment you touch the second island, 
    # distance becomes 4. But, you need the distance just before touching the second island.
    return -1

def _explore_dfs(grid, row, col, visited):
    if row < 0 or row == len(grid):
        return visited
    if col < 0 or col == len(grid[0]):
        return visited
    
    if grid[row][col] == 'W':
        return visited
    
    if (row, col) in visited:
        return visited
    visited.add((row, col))

    neighbors = [
        (row+1, col),
        (row-1, col),
        (row, col+1),
        (row, col-1)
    ]
    for neighbor in neighbors:
        row, col = neighbor
        _explore_dfs(grid, row, col, visited)
    return visited


grid = [
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["L", "L", "W", "W", "L"],
  ["W", "L", "W", "W", "L"],
  ["W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W"],
]
print(best_bridge(grid)) # -> 2