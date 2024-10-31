### Problem
Given a prerequisites list of tuples, tell whether it is possible to take all the courses/not.
![image](https://github.com/user-attachments/assets/ad9da3e4-f5d2-4aea-a977-e795585bb7ab)

### Solution
It's just the cycle detection problem with one change.</br>
If cycle is detected, it means all the courses can't be taken, hence return `False`.</br>
If cycle is not detected, it means all the courses can be taken, hence return `True`.</br>

```python
def prereqs_possible(num_courses, prereqs):
    graph = _build_graph(num_courses, prereqs)

    grey = set()
    black = set()
    for node in graph:
        if _cycle_detect(graph, node, grey, black) == True:
            return False
    return True
```
