def longest_path(graph):
    visited = {}
    longest = float("-inf")
    for node in graph:
        curr_longest = _explore_dfs(graph, node, visited)
        longest = max(curr_longest, longest)
    return longest 

def  _explore_dfs(graph, node, visited):
    # Base case
    if graph[node] == []:
        return 0 
    if node in visited:
        return visited[node]
    else:
        visited[node] = 0

    # Recursive calls
    neighbor_distances = set()
    for neighbor in graph[node]:
        neighbor_distances.add(_explore_dfs(graph, neighbor, visited)) 
    visited[node] = 1 + max(neighbor_distances)

    return visited[node]

graph = {
  'a': ['b', 'd'],
  'b': ['c'],
  'c': [],
  'd': ['b'],
}
print(longest_path(graph)) # -> 3