def longest_path(graph):
    visited = set()
    longest = float("-inf")
    for node in graph:
        curr_longest = _explore_dfs(graph, node, 0, visited)
        longest = max(curr_longest, longest)
    return longest 

def  _explore_dfs(graph, node, distance, visited):
    # Base case
    if graph[node] == []:
        return 0 
    if node in visited:
        return distance
    else:
        visited.add(node)
        distance = 1

    # Recursive calls
    neighbor_distances = set()
    for neighbor in graph[node]:
        neighbor_distances.add(_explore_dfs(graph, neighbor, distance, visited)) 
    max_distance_neighbor = max(neighbor_distances)
    distance += max_distance_neighbor

    return distance

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}
print(longest_path(graph)) # -> 2