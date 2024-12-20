#### Programmatic representation of directed graph
Programatically, directed graph is represented by dictionary. In graph terms, this dictionary is called as `Adjacency list`.</br>
`nodes` are `keys` & `neighbors` are corresponding `values`.</br>
![image](https://github.com/user-attachments/assets/74d74472-da32-4be9-85c2-440ff311403d)
```python
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}
```
#### How to traverse the directed graph?
There are 2 algorithms to traverse directed graph. They are:</br>
<ins>DFS - Depth First Search</ins></br>
- Let's assume you started from node `a` to explore the graph.
- Pick any one of the neighbor & explore the path connected to that neighor fully before coming to next neighbor.</br>

<ins>BFS - Breadth First Search<ins></br>
- Let's assume you started from node `a` to explore the graph.
- Explore all the neighbors of `a` one after the other.

![graphs](https://github.com/user-attachments/assets/e7ca79cf-6ddc-4a2d-bc1c-75a185909089)

#### Why DFS & BFS are exploring the graph in different ways?
![stack](https://github.com/user-attachments/assets/9ee2b1ad-3f4b-466e-ae80-6e78e348460b)
<ins>Note:</ins></br>
Node `a` has 2 neighbors named `b` & `c`.</br>
- While exploring with DFS, if you want to explore the path of node `b` first, then push `b` into the stack at last(after pushing all other neighours).</br>
- Where as while exploring with BFS, if you want to explore the path of node `b` first, then push `b` into the queue at first(before pushing all other neighours).






