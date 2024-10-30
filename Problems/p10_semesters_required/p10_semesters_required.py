def semesters_required(num_courses, prereqs):
    graph = _build_graph(num_courses, prereqs)

    visited = {}
    longest = float("-inf")
    for course in graph:
        curr_longest = _explore_dfs(graph, course, visited)
        longest = max(curr_longest, longest)
    return longest

def  _explore_dfs(graph, course, visited):
    # Base case
    if graph[course] == []:
        return 1
    if course in visited:
        return visited[course]
    else:
        visited[course] = 0

    # Recursive calls
    neighbor_courses = set()
    for neighbor in graph[course]:
        neighbor_courses.add( _explore_dfs(graph, neighbor, visited)) 
    visited[course] = 1 + max(neighbor_courses)

    return visited[course]

def _build_graph(num_courses, prereqs):
    graph = {} 
    for course in range(num_courses):
        graph[course] = []        
    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)  
    return graph

num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
print(semesters_required(num_courses, prereqs)) # -> 3


