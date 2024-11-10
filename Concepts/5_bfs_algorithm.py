# bfs algorithm means, immediately remember
# from collections import deque
# queue = deque([root])
# popleft()
# append()

from collections import deque

def bfs_print(graph, root):
    queue = deque([root])
    while len(queue) > 0: 
        curr = queue.popleft()
        print(curr)
        for neighbor in graph[curr]:
            queue.append(neighbor)

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

bfs_print(graph, "a") # a, b, c, d, e, f
