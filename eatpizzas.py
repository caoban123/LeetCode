import math
pizzas = [1,2,3,4,5,6,7,8]
pizzas.sort()

n = len(pizzas)
odds, evens, ans = n//4 - n//8, n//8, 0

for _ in range(odds): 
    ans+= pizzas.pop()

for _ in range(evens):
    pizzas.pop()
    ans+= pizzas.pop()
print(ans)
    

