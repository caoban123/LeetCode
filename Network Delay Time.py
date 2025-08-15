import heapq


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
adj = {i: [] for i in range(1, n + 1)}
for u, v, w in times:
    adj[u].append((v, w))
print(adj)
    


def dijkstra(n, adj, k):
    dist = [float("inf")] * (n + 1)
    dist[k] = 0
    heap = [(0, k)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist[1:]
dijkstra(n, adj, k)
          




