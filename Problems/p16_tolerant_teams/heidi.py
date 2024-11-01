def build_graph_using_num_cources(num_courses, prereqs):
    graph = {}
    for course in range(0, num_courses+1):
        graph[course] = []
    for a, b in prereqs:
        graph[a].append(b)
    print(graph)

def build_graph_using_a_and_b(prereqs):
    graph = {}
    for a, b in prereqs:
        if a in graph:
            graph[a].append(b)
        else:
           graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
           graph[b] = [a]  
    print(graph)

num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
build_graph_using_num_cources(num_courses, prereqs)
build_graph_using_a_and_b(prereqs)
