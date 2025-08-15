import math
time = [15,63,451,213,37,209,343,319]
lst = [0] * 61
for i in time:
    lst[i % 60] += 1
cnt = 0
if lst[0] > 1:
    cnt += (math.factorial(lst[0])) // (2 * math.factorial(lst[0] - 2))
if lst[30] > 1:
    cnt += (math.factorial(lst[30])) // (2 * math.factorial(lst[30] - 2))
for i in range(1, 30):
    cnt += lst[i] * lst[60 - i]
print(cnt)
