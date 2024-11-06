def topological_order(graph):
    num_parents = _build_parents_graph(graph)
    
    ready = [node for node in num_parents if num_parents[node] == 0]
    order = []
    while ready:
        curr_node = ready.pop()
        order.append(curr_node)
        for child in graph[curr_node]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)
    return order

def _build_parents_graph(graph):
    num_parents = {}
    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1
    return num_parents

print(topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
})) # -> ['c', 'a', 'f', 'b', 'd', 'e']