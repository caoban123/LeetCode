costs = [7,3,3,6,6,6,10,5,9,2]
coins = 56

def counting_sort(costs):
    min_val = min(costs)
    max_val = max(costs)
    Range = max_val - min_val + 1
    counting = [0] * Range
    for val in costs:
        counting[val - min_val] += 1
    for i in range(1, len(counting)):
        counting[i] = counting[i] + counting[i - 1]
    output = [0] * len(costs)
    for val in costs[::-1]:
        counting[val - min_val] -= 1
        output[counting[val - min_val]] = val
    return output
costs = counting_sort(costs)
cnt = 0
i = 0

while coins > 0:
    coins -= costs[i]
    if coins < 0:
        break
    cnt += 1
    i += 1
print(cnt)

