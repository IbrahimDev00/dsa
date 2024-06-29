nums = input()
val = int(input())

k = 0
for i in range(len(nums)):
    if val != nums[i]:
        nums[k] = nums[i]
        k += 1
print(k) 