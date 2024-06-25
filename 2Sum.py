""""
Q. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

nums = list(int(input()))
target = int(input())

indices = {}
for key, val in enumerate(nums):
    if target-val in indices:
        print([indices[target-val], nums[val]])
    indices[val] = key
