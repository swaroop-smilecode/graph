def dfs_print(graph, root):
    # Base case
    # It's not needed because, here recursive calls are not going to be initiated
    # infinitely. You are initiating the recursive calls only on neighbors. 

    # Recursive calls
    print(root)
    for neighbor in graph[root]:
        dfs_print(graph, neighbor)

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
dfs_print(graph, "a") # a, b, d, f, c, e
