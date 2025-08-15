isConnected = [[1,0,0],[0,1,0],[0,0,1]]
visited = [0] * len(isConnected[0])

def dfs(u):
    visited[u] = 1
    for i in range(len(isConnected[0])):
        if (isConnected[u][i] or isConnected[i][u]) and not visited[i]:
            dfs(i)
cnt = 0
for i in range(len(isConnected[0])):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)