def dfs(graph, curr_node):
    if not curr_node:
        return []
    if graph[curr_node]:
        for neighbor in graph[curr_node]:
                return [curr_node] + dfs(graph, neighbor)
     

graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

result = dfs(graph, "a")
print(result)