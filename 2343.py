# 기타 레슨

n, m = map(int, input().split())
A = list(map(int, input().split()))


def num_of_blue_ray(length):
    result = 1
    temp = 0
    for item in A:
        temp += item
        if temp > length:
            temp = item
            result += 1
    return result


left, right = max(A), sum(A)
while left <= right:
    medium = (left + right) // 2
    temp_num = num_of_blue_ray(medium)
    if temp_num <= m:
        right = medium - 1
    else:
        left = medium + 1

print(left)
