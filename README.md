# Types of Graphs
There are 2 types of graphs
1. Directed graph
    - Programatically, this graph is represented by dictionary.
      Keys are nodes & corresponding values are it's neighbors
        graph = {
            'f': ['g', 'i'],
            'g': ['h'],
            'h': [],
            'i': ['g', 'k'],
            'j': ['i'],
            'k': []
        }
    - There are 2 types of graphs
      1. Acyclic graph
      2. Cyclic graph

2. Undirected graph
    - Programatically, this graph is represented by list of tuples, where
      each tuple represents one edge. 
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]
    - Even though the graph is given to you in the form of list of tuples, 
      will convert it into graph, so that we can apply same logic of traversing 
      either in case of directed graph/un directed graph.
    - There are 2 types of graphs
      1. Acyclic graph
      2. Cyclic graph

# Types of algorithms to traverse the Graph
1. dfs
2. bfs