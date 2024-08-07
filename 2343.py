# 기타 레슨

n, m = map(int, input().split())
A = list(map(int, input().split()))

left, right = max(A), sum(A)


def NumOfBlueRay(length):
    result = 1
    temp = 0
    for i in A:
        temp += i
        if temp > length:
            temp = i
            result += 1
    return result


while left <= right:
    middle = (left + right) // 2
    if NumOfBlueRay(middle) <= m:
        right = middle - 1
    else:
        left = middle + 1

print(left)
