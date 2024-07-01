# Remove Element

## Question :

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k

## Code:

``` 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k
```
### Explanation :

1. First iterate through the list `nums`
2. Check if the i'th position in `nums` is equal to value or not, if not equal then shift it to k'th position
3. Increment the value of `k` by 1
4. This will ensure that all the elements that are not equal to `val`, are at the start of the list, and the ones equal to `val` are at the end of the list.
5. Repeat the process.