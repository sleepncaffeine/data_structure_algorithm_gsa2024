def DFS(vtx, adj, s, visited):
    print(vtx[s], end=" ")
    visited[s] = True

    for v in range(len(vtx)):
        if adj[s][v] == 1 and not visited[v]:
            DFS(vtx, adj, v, visited)


vtx = ["U", "V", "W", "X", "Y"]
edge = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
]

print("DFS: ", end="")
DFS(vtx, edge, 0, [False] * len(vtx))
print()

# graph:
# U -- W -- Y
# |  /
# | /
# V -- X
