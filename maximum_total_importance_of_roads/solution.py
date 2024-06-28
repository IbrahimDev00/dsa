n = int(input())
roads = list(input())
arr = [0]*n
for a,b in roads:
    arr[a] +=1
    arr[b] +=1
arr.sort()
sumation = 0 
for i in range(n):
    sumation += arr[i] * (i+1)
print(sumation)