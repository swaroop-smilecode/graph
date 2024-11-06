### Problem
Oh-no! You forgot the number combination that unlocks your safe.</br>
Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints</br>
that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y'</br>
that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).
```python
safe_cracking([
  (7, 1),
  (1, 8),
  (7, 8),
]) # -> '718'
```
### Approach
Just convert the edges given to you into graph & apply topological sort. That's it!
![image](https://github.com/user-attachments/assets/e58eed5a-0c9a-44c1-b5f4-2f89828fe819)
