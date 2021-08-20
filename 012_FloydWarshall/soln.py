INF = 99999

def floydWarshall(graph):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)

def printSolution(dist):
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print(99999, end = ' ')
            else:
                print (dist[i][j], end = ' ')
            if j == V-1:
                print()
V = int(input())
graph = []
for i in range(V):
    arr = list(map(int, input().rstrip().split()))
    graph.append(arr)
# print(graph)
floydWarshall(graph)

