# Three Consecutive odd [Problem 1550.]

## Question:

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

## Code:

```python
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    odd = 0
    for i in arr:
        if i%2 != 0:
            odd += 1
            if odd == 3:
                return(True)
        else:
            odd = 0
    return(False)
```

### Explanation:

#### Variable Initialization

`odd = 0`
A variable odd is initialized to 0. This variable will keep track of the number of consecutive odd numbers encountered.
Iteration through the List

`for i in arr:`
A for-loop is used to iterate over each element i in the list arr.

#### Check if the Number is Odd

    ```
        if i % 2 != 0:
            odd += 1
            if odd == 3:
                return True
        else:
            odd = 0
    ```
The code checks if the current number i is odd using the condition `i % 2 != 0`.
If i is odd, it increments the odd counter by 1.
If the odd counter reaches 3, it means there are three consecutive odd numbers, and the method returns True.
If i is not odd, the odd counter is reset to 0.
Return False if No Three Consecutive Odds Found


`return False`
If the loop completes without finding three consecutive odd numbers, the method returns False.