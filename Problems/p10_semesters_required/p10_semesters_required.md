### Problem
What are the minimum number of semisters that are required to take all the courses?</br>
prerequisites are represented as list of tuples where first element of tuple is course & the second element is prerequisite. An example is:</br>
```python
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
```
If you satisfy the prerequisites, there is no limit on how many number of courses can be taken in single semister.
### Solution
First convert the given input into `graph`, which makes the problem into dictionary.
Remember that this dictionary is called as `Adjacency list` in graph terms.
![image](https://github.com/user-attachments/assets/659dc9ef-8256-4e29-9100-8c852535cb2b)
Also, notice that if this problem had any cycle, it would have been impossible to take all the courses.</br>
You cannot take all the courses, because you can't take any course inside the cycle.</br>
For example, consider `5`. To take `5`, prerequisite is `6`, prerequisite is `2`, prerequisite is `5`.
![image](https://github.com/user-attachments/assets/73641325-1ccd-4c8c-9477-bfac82524ad6)
#### Let's see how many semisters are required to take all the courses.
For the first semister, you can only take the courses which don't have prerequisites.
![image](https://github.com/user-attachments/assets/e708377a-df78-422c-b790-dbc2314b7f02)
In semister 2, some more courses are unlocked.
![image](https://github.com/user-attachments/assets/57e6e2a6-eec7-4d96-85d7-6d668b9bec69)
In semister 3, some more courses are unlocked.
![image](https://github.com/user-attachments/assets/3c3ba7aa-7535-40ad-90a7-830bc9bc4bf2)
In semister 4, some more courses are unlocked.
![image](https://github.com/user-attachments/assets/7b42a03c-3fb0-4d82-9424-aa98cb30ab7d)
