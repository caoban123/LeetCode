nums = [4,5,6]
maxx = float('-inf')

for i in range(len(nums) - 1):
    if nums[i + 1] == nums[i] + 1:
        cnt = 0
        x = i
        flag = 0
        while True:
            if not flag:
                if x < len(nums) - 1 and nums[x] + 1 == nums[x + 1]:
                    cnt += 1
                    x += 1
                    flag = 1
                    continue
                else:
                    maxx = max(maxx, cnt)
                    break
            else:
                if x < len(nums) -1 and nums[x] - 1 == nums[x + 1]:
                    cnt += 1
                    x += 1
                    flag = 0
                    continue
                else:
                    maxx = max(maxx,cnt)
                    break
print(maxx + 1)


