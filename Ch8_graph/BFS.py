from queue import Queue


def BFS_AL(vtx, alist, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=" ")
        for v in alist[s]:
            if not visited[v]:
                Q.put(v)
                visited[v] = True


vtx = ["U", "V", "W", "X", "Y"]
edge = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 4],
    [1],
    [2],
]

print("BFS: ", end="")
BFS_AL(vtx, edge, 0)
print()
