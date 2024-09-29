def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if traverse_graph(graph, node, visited) == True:
            count += 1
    return count

def traverse_graph(graph, src, visited):
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        traverse_graph(graph, neighbor, visited)
    return True
    
graph = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}
print(connected_components_count(graph)) # -> 2