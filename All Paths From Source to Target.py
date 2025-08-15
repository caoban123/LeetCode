graph = [[1,2],[3],[3],[]]
n = len(graph)
visited = [0] * 20
list = []
def dfs(graph, n, path, visited, u):
    visited[u] = 1
    path.append(u)
    if u == n - 1:
        list.append(path[:])
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, n, path, visited, v)
    visited[u] = 0
    path.pop()
dfs(graph, n, [], visited, 0)
print(list)
            
