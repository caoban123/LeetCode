n = 4
edges = [[0,1,5],[1,2,5],[2,3,5]]
k = 4

lst = []

edges.sort(key = lambda x: x[2])
sz = [1 for i in range(n)]
parent = [i for i in range(n)]
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if sz[x] < sz[y]:
            parent[x] = y
            sz[y] += sz[x]
        else:
            parent[y] = x
            sz[x] += sz[y]
        return True
comp = n
threshold = 0

for u, v, w in edges:
    if comp <= k:
        break
    if union(u, v):
        comp -= 1
    threshold = w 
print(threshold)

