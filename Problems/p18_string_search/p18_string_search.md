### Problem
If there is a path in this graph which has `HELLO`, `return True` else `return False`.
![image](https://github.com/user-attachments/assets/e38f0a20-710b-4a24-8037-98a31df73b5e)

### Approach
- Problem is not asking you `closest path` / `smallest path`. Hence go with `DFS`.
- Will use some iterative code to iterate through grid starting from `cell (0,0)` & during this iterations,</br>
  will check whether the value inside the cell is `H`?
  ![image](https://github.com/user-attachments/assets/30ee3df5-7d81-45a1-9f3b-b18d4a4bf8de)
- Once you find the `H`, initiate DFS starting from that cell
  ![image](https://github.com/user-attachments/assets/703ebffa-b767-4547-8c3e-ed530c8496d4)
