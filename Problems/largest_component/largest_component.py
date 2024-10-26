def largest_component(graph):
    visited = set()
    count = 0
    for node in graph:
        count += traverse_graph(graph, node, visited, 0)
    print(count)

def traverse_graph(graph, src, visited, count):
    if src in visited:
        return 0
    visited.add(src)
    count = 1
    for neighbor in graph[src]:
        count += traverse_graph(graph, neighbor, visited, count)
    return count
    
largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) # -> 6
