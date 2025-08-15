graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
visited = [0] * len(graph)
list = []
def dfs(u):
    if visited[u] != 0:
        return visited == 2
    visited[u] = 1
    for v in graph[u]:
        if not dfs(v):
            return False
    visited[u] = 2
    return True
lst = [i for i in range(len(graph)) if dfs(i)]
print(lst)

                