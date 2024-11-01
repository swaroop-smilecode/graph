def can_color(graph):
    coloring = {}
    for node in graph:
        if _can_color(graph, node, coloring, "red") == True:
            continue
        return False

def  _can_color(graph, node, coloring, curr_color):
    if node in coloring:
        if coloring[node] == curr_color:
            return True
        return False
    
    coloring[node] = curr_color

    for neighbor in graph[node]:
        if curr_color == "red":
            curr_color = "blue"
        elif curr_color == "blue":
            curr_color = "red"
        if _can_color(graph, neighbor, coloring, curr_color) == True:
            continue
        return False
    return True

print(can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
})) # -> True
