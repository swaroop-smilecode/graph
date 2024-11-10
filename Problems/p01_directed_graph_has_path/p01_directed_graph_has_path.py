def has_path(graph, src, dst):
    # Base case
    if src == dst:
        return True

    # Recursive calls
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True
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
