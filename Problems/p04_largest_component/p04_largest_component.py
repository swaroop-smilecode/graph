def largest_component(graph):
    visited = set()
    largest = 0
    for node in graph:
        curr_largest = _explore_dfs(graph, node, visited)    
        largest = max(largest, curr_largest)
    return largest

def _explore_dfs(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += _explore_dfs(graph, neighbor, visited)
    return size      


print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 4