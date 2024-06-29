"""Q.) Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k."""

nums = input()
val = int(input())

k = 0
for i in range(len(nums)):
    if val != nums[i]:
        nums[k] = nums[i]
        k += 1
print(k) 