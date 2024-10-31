def has_cycle(graph):
    grey = set()
    black = set()
    for node in graph:
        if _has_cycle(graph, node, grey, black) == True:
            return True
    return False

def _has_cycle(graph, node, grey, black):
    if node in black:
        return False
    
    if node in grey:
        return True
    grey.add(node)
    for neighbor in graph[node]:
        if _has_cycle(graph, neighbor, grey, black) == True:
            return True
    grey.remove(node)
    black.add(node)
    
    return False

print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})) # -> True