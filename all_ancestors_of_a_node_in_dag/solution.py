n = int(input())
edges = input()
graph = [[] for _ in range(n)]
indegree = [0]*n

for a,b in edges:
    graph[a].append(b)
    indegree[b] +=1

topo_order = []
stack = [i for i in range(n) if indegree[i] == 0]
while stack:
        node = stack.pop()
        topo_order.append(node)

        for neighbor in graph[node]:
              indegree -=1
              if indegree[neighbor] == 0:
                    stack.append(neighbor)

ancestors = [set() for _ in range(n)]
for node in topo_order:
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
            
            result = [sorted(list(ancestors[i])) for i in range(n)]

            print(result)
             