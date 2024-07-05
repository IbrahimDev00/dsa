# Maximum total importance of roads

## Question:

You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.

## Code

```python 

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0]*n
        for a,b in roads:
            arr[a] +=1
            arr[b] +=1
        arr.sort()
        suma = 0
        for i in range(n):
            suma += arr[i] *(i+1)
        return(suma)
```

### Explanation:

`arr`: An array of size n initialized to zero. This array will keep track of the number of roads connected to each city.

Iterate through each road represented by a pair [A, B].

For each road, increment the count for both cities A and B.

Sort the array `arr` in ascending order. After sorting, cities with fewer roads will be at the beginning, and cities with more roads will be at the end.

nitialize a variable sumation to store the total importance.

Iterate through the sorted array `arr`.

Multiply the number of roads for each city (`arr[i]`) by its assigned importance value (`i + 1`), and add this to sumation.

