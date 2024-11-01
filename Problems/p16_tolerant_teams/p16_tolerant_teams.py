def tolerant_teams(rivalries):
    graph = _build_graph(rivalries)

    team = {}
    # To explore all the sub graphs of given graphs.
    for node in graph:
        if node not in team:
            if _tolerant_teams(graph, node, team, "red"):
                continue
            else:
                return False
    return True

def _tolerant_teams(graph, node, team, color):
    # Base case:
    if node in team:
        return team[node] == color
    
    team[node] = color

    if color == "red":
        color = "blue"
    elif color == "blue":
        color = "red"
    # Recursive calls.
    # These are needed to explore each sub graph, through the neighbors 
    # of the node. This initial node of the graph will be received into
    # this function as function parameter.
    for neighbor in graph[node]:
        if _tolerant_teams(graph, neighbor, team, color):
            continue
        return False
    return True

def _build_graph(rivalries):
    graph = {}
  
    for a, b in rivalries:
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]   

    return graph

print(tolerant_teams([
  ('philip', 'seb'),
  ('raj', 'nader')
])) # -> True