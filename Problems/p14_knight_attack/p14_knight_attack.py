# After looking at the solution, you may ask there is no minimum logic?
# If you are implementing BFS, first time you hit the goal is nothing 
# but the minimum value.

from collections import deque
def knight_attack(n, kr, kc, pr, pc):
    queue = deque([(kr, kc, 0)])
    visited = set()
    while queue:
        kr, kc, moves = queue.popleft()
        if kr < 0 or kr >= n:
            continue
        if kc < 0 or kc >= n:
            continue
        
        if (kr, kc) == (pr, pc):
            return moves

        if (kr, kc) in visited:
            continue
        else:
            visited.add((kr, kc))

        neighbors = [
            ( kr + 2, kc + 1 ),
            ( kr - 2, kc + 1 ),
            ( kr + 2, kc - 1 ),
            ( kr - 2, kc - 1 ),
            ( kr + 1, kc + 2 ),
            ( kr - 1, kc + 2 ),
            ( kr + 1, kc - 2 ),
            ( kr - 1, kc - 2 ),
        ]
        for neighbor in neighbors:
            kr, kc = neighbor
            queue.append((kr, kc, moves+1))

    return None

print(knight_attack(8, 1, 1, 2, 2)) # -> 2