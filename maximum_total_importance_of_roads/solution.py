"""Q.)You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally."""

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