vtx = ["U", "V", "W", "X", "Y"]
adg = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
]
visited = [False] * 5


def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adg[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end=" ")
                ST_DFS(vtx, adj, v, visited)


ST_DFS(vtx, adg, 0, visited)
print()
"""
U     W --- Y
|   / 
| /   
V --- X
"""

INF = 999


def getMinVertex(dist, selected):
    minv = 0
    mindist = INF
    for v in range(len(dist)):
        if selected[v] == False and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv


def MSTPrim(vertex, adj):
    n = len(vertex)
    dist = [INF] * n
    dist[0] = 0
    selected = [False] * n

    for _ in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=" ")

        for v in range(n):
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

        print(": ", dist)


vertex = ["A", "B", "C", "D", "E", "F", "G"]
matrix = [
    [INF, 25, INF, 12, INF, INF, INF],
    [25, INF, 10, INF, 15, INF, INF],
    [INF, 10, INF, INF, INF, INF, 16],
    [12, INF, INF, INF, 17, 37, INF],
    [INF, 15, INF, 17, INF, 19, 14],
    [INF, INF, INF, INF, 14, INF, 42],
    [INF, INF, 16, 37, 14, 42, INF],
]

MSTPrim(vertex, matrix)
