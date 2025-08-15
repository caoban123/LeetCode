import heapq

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
map = {i: [] for i in range(n)}
for u, v, money in flights:
    map[u].append((v, money))

def findCheapestPrice(n, graph, src, dst, k):
    heap = [(0, src, 0)] 
    visited = {}
    while heap:
        cost, node, stops = heapq.heappop(heap)
        if node == dst:
            return cost
        if (node in visited and visited[node] <= stops) or stops > k:
            continue
        visited[node] = stops
        for neighbor, price in graph[node]:
            heapq.heappush(heap, (cost + price, neighbor, stops + 1))
                
    return -1
print(findCheapestPrice(n, map, src, dst, k))



