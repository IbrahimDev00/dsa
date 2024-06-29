"""Q.) You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges."""

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
             