# Search insert position [Problem 35.]

## Question:

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

## Code:

#### Python
``` 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1 
        return l

```
#### Go
``` 
func searchInsert(nums []int, target int) int {
    l := 0
    r := len(nums) -1
    for l<=r{
        m := l +(r-l)//2
        if target > nums[m]{
            l = m+1
        } else{
            r = m-1
        }
    }
    return l
}
```


