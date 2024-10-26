def minimum_island(grid):
    # It is undirected graph, so have a visited set to stop visiting already visited nodes
    visited = set()
    # End goal of this algo is to find minimum? Then initiate min_size with float("inf")
    # End goal of this algo is to find maximum? Then initiate max_size with float("-inf")
    min_size = float("inf")

    # Navigate through each cell of the grid one after the other & initiate an DFS for each cell
    # The purpose of this DFS call is to find the size of island and return it.
    rows = len(grid)
    cols = len(grid[0])
    for row in range(0, rows):
        for col in range(0, cols):
              size = explore_size(grid, row, col, visited)
              # Logic to update the min_size, each time you get the island size from DFS call 
              if size > 0 and size < min_size:
                min_size = size
    print(min_size)

def explore_size(grid, row, col, visited):
  # The goal of this DFS is to return size, which is number(See the last line of this fn which is
  # "return size"). 
  # Hence, the base case also should return number, because, if you return any other type, 
  # then it will affect the operation which is performed inside the "minimum_island" function 
  # based on the return value of this DFS. 

  # When i said code inside the "minimum island" function means:
  # size = explore_size(grid, row, col, visited)
  # if size > 0 and size < min_size:
  # min_size = size

  # And this return value should be 0, the reason is: hitting the base case means, 
  # you do not want to do any work, instead just get out from this function. Because of
  # this reason, mostly base cases return value will either be 0 / False.

  # This base case is to check whether the cell we are working on currently is within 
  # the limits of grid/not? This should be first base case, becasue, if the cell is not 
  # within limits of grid, There is no question of doing further work in this DFS call.
  if (row < 0 or row == len(grid) or
     col < 0 or col == len(grid[0])):
    return 0
  
  # This base case is to check whether the cell we are working on currently is Land / Water?
  # If "W", then we are not interested in doing any work in this DFS call. Hence return 0
  if grid[row][col] == "W":
     return 0
  
  # This base case is to check whether the cell we are currently working on is already visited/not?
  # If visited, it means, you did work related to that cell already. 
  # Then no need to do any additional work. return 0
  # If not visited, Then first add it to visited set & start the work.
  position = (row, col)
  if position in visited:
     return 0
  visited.add(position)
  # This is the work we are doing in this DFS call.
  # As of now you reached this place means, you are on an unexplored cell, so, count that 
  # cell through size variable and then start exploring it's neighbors. 
  # If it's neighbours are any unvisited land cells, then that DFS call also will return 
  # 1, so add that to the size. 
  size = 1
  size += explore_size(grid, row - 1, col, visited)
  size += explore_size(grid, row + 1, col, visited)  
  size += explore_size(grid, row, col - 1, visited)
  size += explore_size(grid, row, col + 1, visited)
  return size

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2