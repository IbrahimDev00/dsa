nums = list(int(input()))
target = int(input())

indices = {}
for key, val in enumerate(nums):
    if target-val in indices:
        print([indices[target-val], nums[val]])
    indices[val] = key
