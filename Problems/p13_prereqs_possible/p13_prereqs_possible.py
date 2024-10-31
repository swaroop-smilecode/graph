def prereqs_possible(num_courses, prereqs):
    graph = _build_graph(num_courses, prereqs)

    grey = set()
    black = set()
    for node in graph:
        if _cycle_detect(graph, node, grey, black) == True:
            return False
    return True

def _cycle_detect(graph, node, grey, black):
    if node in black:
        return False
    if node in grey:
        return True
    grey.add(node)
    for neighbor in graph[node]:
        if _cycle_detect(graph, neighbor, grey, black) == True:
            return True        
    grey.remove(node)
    black.add(node)
    return False

def _build_graph(num_courses, prereqs):
    graph = {}

    for course in range(0, num_courses):
        graph[course] = []

    for a, b in prereqs:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    return graph

num_courses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
print(prereqs_possible(num_courses, prereqs)) # -> True