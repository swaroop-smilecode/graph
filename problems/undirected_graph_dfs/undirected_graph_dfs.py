def undirected_path(edges, src, dst):
    graph = build_graph(edges)
    return has_path(graph, src, dst, set())

def build_graph(edges):
    graph = {}

    for edge in edges:
        a,b = edge
        if a not in graph:
          graph[a] = []
        if b not in graph:
          graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbor in graph[src]:
      if has_path(graph, neighbor, dst, visited) == True:
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