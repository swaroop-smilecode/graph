def undirected_path(edges, src, dst):
    graph = _build_graph(edges)
    return _undirected_path(graph, src, dst, set())

def _build_graph(edges):
    graph = {}
    for a, b in edges:
      if a in graph:
          graph[a].append(b)
      else:
          graph[a] = [b]
      if b in graph:
          graph[b].append(a)
      else:
          graph[b] = [a]
    return graph

def _undirected_path(graph, src, dst, visited):
    # To avoid infinite loop
    if src in visited:
        return None
    else:
        visited.add(src)

    # Base case:
    if src == dst:
        return True
    
    # Recursive calls
    for neighbor in graph[src]:
        if _undirected_path(graph, neighbor, dst, visited) == True:
            return True
    return False

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
print(undirected_path(edges, 'j', 'm')) # -> True