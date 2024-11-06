### Problem
If there is a path in this graph which has `HELLO`, `return True` else `return False`.
![image](https://github.com/user-attachments/assets/e38f0a20-710b-4a24-8037-98a31df73b5e)
### Approach overview
- Problem is not asking you `closest path` / `smallest path`. Hence go with `DFS`.
- Will use some iterative code to iterate through grid starting from `cell (0,0)` & during this iterations,</br>
  will check whether the value inside the cell is `H`?
  ![image](https://github.com/user-attachments/assets/30ee3df5-7d81-45a1-9f3b-b18d4a4bf8de)
- Once you find the `H`, initiate DFS starting from that cell
  ![image](https://github.com/user-attachments/assets/703ebffa-b767-4547-8c3e-ed530c8496d4)
### Let's start coding
Starting from `cell (0,0)`, will initiate DFS on each cell with the help of iterative code.</br>
- If any one of the DFS call returns `True`, it means we found `HELLO`</br>
- Even after iterating through entire grid, if we don't receive even one single `True`, then return `False`,</br>
  to indicate that we searched for word `HELLO` starting from each & every cell of the grid, but did not find such word.
```python
def string_search(grid, s):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # You are initiating the DFS recursive call on each & every cell.
            # If atleast one of the DFS recursive call returns True, that means you found HELLO
            # Hence return True
            visited = set()
            if dfs(grid, r, c, s, visited) == True:
                return True
    
    # Look at the above iteration code. 
    # You iterated through each & every cell & looked for HELLO.
    # If any one of that DFS call would have returned True, it means you found HELLO, hence return True as
    # main return for this function.
    # But, if you reach here, that means you did not find HELLO in any of the DFS call.
    # Then return False, which indicates that there is no path in the grid which has HELLO.
    return False
```
Coming to helper function
```python
def dfs(grid, r, c, s, visited):
    # First check whether the cell you are currently working on is out of bound?
    if r < 0 or r == len(grid):
        return False
    if c < 0 or c == len(grid[0]):
        return False

    # To stop visiting the same cell which you visited previously.
    if (r, c) in visited:
        return False
    else:
        visited.add((r, c))

    # Graph problems will have n number of base cases.
    # All the base cases will return False, except the Affirmative one.
    # This is that Affirmative base case.

    # You will search for the required word character by character.
    # During that search what if you find HELLO?
    # You don't have any thing to search for, right?
    # Then return True as you found what you need to found.

    # This checking for empty input should be the first condition immediatly after the 
    # out of bound condition check & visited check.
    # The reason is: later code works on the input.
    if s == "":
        return True

    # If the character at current cell is not required character?
    if grid[r][c] != s[0]:
        return False

    # Remaining word to be searched for in the recursive calls.
    remaining_word = s[1:]

    # Recursive calls
    neighbors = [(r+1, c), 
                 (r-1, c), 
                 (r, c+1), 
                 (r, c-1)
                ]
    for neighbor in neighbors:
        r, c = neighbor
        visited = set()
        # If i am able to find the remaining word, then this DFS call returns True
        # Once you get True from this DFS call, just return that True as a return for this function.
        if dfs(grid, r, c, remaining_word, visited) == True:
            return True

    # Look at the above step. You iterated through each neighbor & looked for remaining word.
    # If any one of the DFS recursive call would have returned True, you will receive True & 
    # you won't be coming here.
    # But, if you reach here, that means you did not find the remaining word in any of the DFS recursive call.
    # Then return False, which indicates that there is no path in the grid which has HELLO.
    return False
```
