# 셀프 넘버

nums = [i for i in range(1, 10001)]

for num in range(1, 10001):
    new = num
    tmp = str(num)
    for i in range(len(tmp)):
        new += int(tmp[i])
    if new in nums:
        nums.remove(new)

for num in nums:
    print(num)