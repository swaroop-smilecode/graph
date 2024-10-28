# Idea:
# _explore_dfs function will recieve a node & set.
# It will explore the path connected to that node in dfs manner & while 
# exploring, it will add explored nodes to set.
# During this exploration, if it touches any already visited node, it means 
# that the island is visited already, hence return 0, if not, at the end of 
# function return 1

# In the main function named connected_components_count, you will collect those
# 1's returned from _explore_dfs function & add them which results in total 
# islands count.

def connected_components_count(graph):
    count = 0
    visited = set()
    for node in graph:
        count += _explore_dfs(graph, node, visited)
    return count

def _explore_dfs(graph, src, visited):
    if src in visited:
        return 0
    visited.add(src)
    for neighbor in graph[src]:
        _explore_dfs(graph, neighbor, visited)
    return 1

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