def dfs_print(graph, curr):
    # Base case
    # It's not needed because, here recursive calls are not going to be initiated
    # infinitely. You are initiating the recursive calls only on neighbors. 

    # Recursive calls
    for neighbor in graph[curr]:
        dfs_print(graph, neighbor)
        print(neighbor)


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

dfs_print(graph, "a")