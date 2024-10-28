from collections import deque

def shortest_path(edges, node_a, node_b):
    graph = _build_graph(edges)

    visited = set()
    queue = deque([(node_a, 0)])
    while queue:
        curr_node, distance = queue.popleft()
        if curr_node == node_b:
            return distance
        if curr_node in visited:
            continue
        else:
            visited.add(curr_node)

        for neighbor in graph[curr_node]:
            queue.append((neighbor, distance+1))
    return -1

def _build_graph(edges):
    graph = {}

    for a, b in edges:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    return graph


edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
print(shortest_path(edges, 'w', 'z')) # -> 2