# 기타 레슨

n, m = map(int, input().split())
A = list(map(int, input().split()))


def NumOfBlueRay(size):
    blue_ray = 1
    temp = 0
    for i in A:
        temp += i
        if temp > size:
            temp = i
            blue_ray += 1
    return blue_ray


left, right = max(A), sum(A)
while left <= right:
    median = (left + right) // 2
    num_of_blue_ray = NumOfBlueRay(median)
    if num_of_blue_ray <= m:
        right = median - 1
    else:
        left = median + 1

print(left)

