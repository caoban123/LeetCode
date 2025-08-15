queries = [3,1,2,1]
m = 5
P = [i for i in range(1, m + 1)]
ans = []
for num in queries:
    ans.append(P.index(num))
    x = P.pop(P.index(num))
    P.insert(0, x)
print(ans)
