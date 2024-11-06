def safe_cracking(edges):
    num_parents, graph = _build_parents_graph(edges)
    
    ready = [node for node in num_parents if num_parents[node] == 0]
    order = ""
    while ready:
        curr_node = ready.pop()
        order += str(curr_node)
        for child in graph[curr_node]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)
    return order

def _build_parents_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = [] 
        if b not in graph:
            graph[b] = []
        graph[a].append(b)

    num_parents = {}
    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1
    return num_parents, graph

print(safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
])) # -> '718'
