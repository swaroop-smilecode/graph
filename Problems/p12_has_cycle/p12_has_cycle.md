### Problem
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph.</br>
The function should return a boolean indicating whether or not the graph contains a cycle.</br>
### Approach
Will use `White-Grey-Black` cycle detection algorithm.
![Presentation1](https://github.com/user-attachments/assets/e1755637-3d7d-44be-a395-a574e825560b)

When exploring the graph like this, if we hit an `grey` node, it means, there is a cycle.
![image](https://github.com/user-attachments/assets/44d662bf-d9ba-4787-956b-0caf37b36e06)
