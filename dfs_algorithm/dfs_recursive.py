def dfs(graph, curr_node):
    if not graph:
        return []

    if graph[curr_node]:
        for neighbor in graph[curr_node]:
            partial_path = dfs(graph, neighbor)
    return partial_path

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