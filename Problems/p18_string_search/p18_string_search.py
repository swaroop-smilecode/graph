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


grid = [
    ['e', 'y', 'h', 'i', 'j'],
    ['q', 'x', 'e', 'r', 'p'],
    ['r', 'o', 'l', 'l', 'n'],
    ['p', 'r', 'x', 'o', 'h'],
    ['a', 'a', 'm', 'c', 'm']
]
print(string_search(grid, 'hello')) # -> True