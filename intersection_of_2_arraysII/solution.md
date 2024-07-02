# Intersection of two arrays II [Problem 350.]


## Question:

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

## Code:

#### Python
```
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        a = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                a.append(nums1[i])
                i +=1
                j +=1
        return a

```
#### Go
```
func intersect(nums1 []int, nums2 []int) []int {
    countMap := make(map[int]int)
    for _, num := range nums1 {
        countMap[num]++
    }
    
    result := []int{}
    
    for _, num := range nums2 {
        if count, found := countMap[num]; found && count > 0 {
            result = append(result, num)
            countMap[num]-- 
        }
    }

    return result
}

```

### Explanation:

**1. Sorting the Arrays:** Both `nums1` and `nums2` are sorted using `sort.Ints`.

**2. Initialization:** Initialize `i` and `j` to 0.

**3. Loop Through Arrays:** Use a `for` loop that continues as long as both `i` and `j` are within the bounds of their respective arrays.

**4. Comparison and Progression:**

`If nums1[i] is less than nums2[j]`, increment i to move to the next element in nums1.
`If nums1[i] is greater than nums2[j]`, increment j to move to the next element in nums2.
`If nums1[i] is equal to nums2[j]`, append the element to result and increment both i and j.