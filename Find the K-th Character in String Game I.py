lst = [i for i in range(1, 9 + 1)]
x = [lst[i] for i in range(len(lst)) if i % 2 != 0]
x.reverse()
x = [x[i] for i in range(len(x)) if i % 2 != 0]
x.reverse()
x = [x[i] for i in range(len(x)) if i % 2 != 0]
print(x)