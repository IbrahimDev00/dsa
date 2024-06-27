edges = []
for _ in range(2):
    edge = list(map(int, input("Enter two integers separated by space: ").split()))
    edges.append(edge)

if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
    print(edges[0][0])
else:
    print(edges[0][1])