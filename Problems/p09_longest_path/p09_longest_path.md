### Problem:
Find the longest path in given graph. 
![image](https://github.com/user-attachments/assets/1e0baf8e-df27-447e-bffa-ccc4e9c925d2)
### Solution:
#### There are 2 important things to be noted here.</br>
1.</br>
Whenever longest path in given graph is asked, it indirectly saying that such a graph is not having an cycle.</br>
Because, you can't find the path length when a graph has cycle inside it. The reason is: if you keep travelling</br>
in the path which has loop, you will get the longest path length as infinity.</br>
2.</br>
Length of the path means, number of edges.
![image](https://github.com/user-attachments/assets/754578da-4af0-4a51-897e-aaa14cf078bb)
#### Idea
We know leaf node is the end of a path inside the tree.</br> 
![image](https://github.com/user-attachments/assets/4d7cb635-19bc-498d-ada2-d72bbde5ba48)
Iterate over each node of the graph & initiate an DFS call, proceed until you hit the leaf node.</br>
When you hit the leaf node, consider it as base case & `return 0`.</br>
Once you hit the base case, the progression to wards the top of the tree starts.</br>
During this time, add `1` to the returned value whenever you cross an edge.</br>
When top of the tree is reached, you will end up with lenght of the path.</br>
Pick `max` of all path lengths.

For example; below figures shown that you started exploration from `node a` & got the path length as `1`.</br>
You need to repeat the same process on each node & pick the max path.</br>
And since it is graph problem, better to have `visisted` set to avoid working on the same node which was
already touched.
![image](https://github.com/user-attachments/assets/3a041de6-d21b-466a-b058-ea5e7af1f560)
