def dfs(graph, curr_node):
    if not graph:
        return []
    
    stack = [curr_node]
    result = []

    while stack:
        curr_node = stack.pop()
        result.append(curr_node)
        if graph[curr_node]:
            for neighbor in graph[curr_node]:
                stack.append(neighbor)

    return result

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