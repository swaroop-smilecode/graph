### Topological order
#### What is Topological order?
It's a sequence where the parents appear before it's children.
For example; below graph has 2 topological sequences.
![image](https://github.com/user-attachments/assets/788e8845-d114-49d2-a054-9b4faffa28cd)

#### Topological order can be generated, if the graph has no cycle
The reason is: Let's consider your graph has a cycle. In order to take the first node from that cycle to put</br>
it into the order result you are preparing, you need to know who is parent & who is child. Inside an cycle</br>
you can't know who is parent & who is child.

#### Approach
- Prepare a dictionary named `parent`, where each node is stored as key & it's parent count as corresponding value.
  ![image](https://github.com/user-attachments/assets/52efac5a-fa91-47d5-8f8e-c337e1560b0f)
- From dictionary, find the all the nodes which don't have any parents & append it to the `ready` list.</br>
  (Observe the name `ready`, the nodes added to this list has no parents, which means they are ready to be added to final result)</br>
- Take out an element from `ready` list & append it to `topo_order` list.</br>
  (`topo_order` list is the final result list)</br>
  Once a node is added to `topo_order`, decrease it's child parent count value by `1`.</br>
  (You need to decrease by `1`, becasue you processed one of the parent. It's like cutting/stemming out it from the graph)   
![image](https://github.com/user-attachments/assets/3bec783f-1316-43a3-a8df-1e1ac593657b)

- Continue this process, until the parents dictionary decomes empty.
