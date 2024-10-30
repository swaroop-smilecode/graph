### Problem
What's the shortest bridge that can be built between 2 islands. For example, as below.
![image](https://github.com/user-attachments/assets/2f62dfda-a87c-4057-9b57-61275b3cc87b)
### Solution
The approach follows as below.
![image](https://github.com/user-attachments/assets/da5dff80-3413-4304-bec7-11181595881a)
First will find any island & mark each cell as `0` in that island. Why to mark with `0`, let's continue the study</br>
and you will know why.
![image](https://github.com/user-attachments/assets/4ed3c05e-e883-4ad5-b93d-c54a6b9639f0)
Let's initiate BFS on each cell of this island & keep incrementing the cell count by `1`, so that when you reach the</br>
destination island, the count will be equal to the shortest distance between the two islands.
The traversal would look like this:
![image](https://github.com/user-attachments/assets/0d05a00e-5181-4afb-9a74-e87473edcf55)

![image](https://github.com/user-attachments/assets/ecde0824-b315-4760-be6a-4666a1543e0a)

![image](https://github.com/user-attachments/assets/5c0049e0-1cd5-4fa8-b093-2227d8555912)
