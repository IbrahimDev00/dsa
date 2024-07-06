# 2582. Pass the Pillow

## Question:

There are `n` people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the` n - 1th` person, then to the `n - 2th` person and so on.
Given the two positive integers `n` and `time`, return the index of the person holding the pillow after `time` seconds.

## Code:

```python 
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycleLen = 2*(n-1)
        time = time%cycleLen
        if time <n:
            return time+1
        else:
            return 2*n - time - 1
``` 

```go 
import "sort"
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    s := append(nums1, nums2...)
    sort.Ints(s)
    l := len(s)
    if l%2 == 0{
        return float64(s[l/2-1]+s[l/2]) / 2.0
    } else{
        return float64(s[l/2])
    }
}

```

## Explanation:

#### Intuition
The problem involves a line of n people passing a pillow from one to another every second. When the pillow reaches the last person, it changes direction and moves back to the first person, continuing this pattern indefinitely. The goal is to find out who holds the pillow after time seconds.

#### Approach

*Understanding the Cycle:*
The pillow moves in a repeating cycle: From the first person to the last person (forward direction).
From the last person back to the first person (backward direction).
Thus, each full cycle consists of 2 * (n - 1) seconds, where the pillow travels forward through all n people and then backward through n-2 people.

*Effective Time:* To simplify the problem, we can reduce the problem to the remainder of time after division by the cycle length. This is because the position after a full cycle is the same as the starting position.

*Calculate the Index:*
When moving forward, the index is simply time + 1.
When moving backward, the index can be calculated as 2*n - time - 1.


#### Complexity
*Time complexity: O(1)*
The solution involves a few arithmetic operations and conditional checks, which are constant-time operations.

*Space complexity: O(1)*
The solution uses a fixed amount of extra space regardless of the input size.