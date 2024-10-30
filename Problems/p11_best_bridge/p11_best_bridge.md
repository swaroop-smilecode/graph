### Problem
What's the shortest bridge that can be built between 2 islands. For example, as below.
![image](https://github.com/user-attachments/assets/2f62dfda-a87c-4057-9b57-61275b3cc87b)
### Solution
The approach follows as below.
![image](https://github.com/user-attachments/assets/da5dff80-3413-4304-bec7-11181595881a)
First will find any one island, explore it & store the indexes of corresponding cells inside an set.</br> 
For example, let's consider that we explored the island marked with red colour dots.</br>
![image](https://github.com/user-attachments/assets/d69786bb-8b1d-4409-9dd4-43ea46a79f35)

Let's initiate BFS on each cell of this island & keep incrementing the cell count by `1`, so that when you reach the</br>
destination island, the count will be equal to the shortest distance between the two islands.
The traversal would look like this:
![image](https://github.com/user-attachments/assets/e4512cdc-38be-45f2-9560-d24dd3c5489e)

![image](https://github.com/user-attachments/assets/fc7f3ba7-f00b-41fd-9ca2-9f6d390435df)

![image](https://github.com/user-attachments/assets/f6902dfe-5f20-4728-81cb-e6fa6cb37217)

![image](https://github.com/user-attachments/assets/f65a3b56-a573-42ef-b3ae-7e478d6c0d4a)
