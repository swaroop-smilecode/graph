def can_color(graph):
    coloring = {}
    for node in graph:
        if node not in coloring:
            # For each node, explore the graph to find out, can you color entire graph with alternative colors.
            # You need to do this for each node, because the graph me be split into parts. So, how do you jump from 
            # one part of the graph to next part? That's by exploring the whole graph for each node.

            # Now,
            # If you receive True? continue exploration of whole graph once again for another node.
            # If you receive falls. That's it. Stop whole algorithm & return False
            if _can_color(graph, node, coloring, "red"):
                continue
            return False
    # If this line is reached, then it means, for each node that is explored, you received True. 
    # Which also means, you can colour complete graph even though it is split into parts.
    # This is the final answer. return True
    return  True

def  _can_color(graph, node, coloring, curr_color):
    if node in coloring:
        if coloring[node] == curr_color:
            return True
        return False
    
    coloring[node] = curr_color

    if curr_color == "red":
        curr_color = "blue"
    elif curr_color == "blue":
        curr_color = "red"
    for neighbor in graph[node]:
        if _can_color(graph, neighbor, coloring, curr_color):
            continue
        return False
    return True

print(can_color({
  "x": ["y"],
  "y": ["x","z"],
  "z": ["y"]
})) # -> True