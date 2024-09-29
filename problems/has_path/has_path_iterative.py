from collections import deque

def has_path(graph, src, dst):
    queue = deque([src])
    
    while queue:
        current_node = queue.popleft()

        if current_node == dst:
            return True
        for neighbor in graph[current_node]:
            queue.append(neighbor)

    return False

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k')) # True

    
    
  

  