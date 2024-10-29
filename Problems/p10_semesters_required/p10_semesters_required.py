def semesters_required(num_courses, prereqs):
    graph = _build_graph(prereqs)

    visited = {}
    longest = float("-inf")
    for course in graph:
        curr_longest = _explore_dfs(graph, course, visited)
        longest = max(curr_longest, longest)
    
    if longest == float("-inf"):
        return 1
    else:
        return longest

def  _explore_dfs(graph, course, visited):
    # Base case
    if graph[course] == []:
        return 1
    if course in visited:
        return visited[course]

    # Recursive calls
    neighbor_courses = set()
    for neighbor in graph[course]:
        neighbor_courses.add( _explore_dfs(graph, neighbor, visited)) 
    max_neighbor_courses = max(neighbor_courses)
    visited[course] = 1 + max_neighbor_courses

    return visited[course]

def _build_graph(prereqs):
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
    return graph

num_courses = 7
prereqs = [

]
print(semesters_required(num_courses, prereqs)) # -> 5