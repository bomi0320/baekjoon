# 문자열
import math

a, b = input().split()

a_len, b_len = len(a), len(b)
gap = b_len - a_len  # a, b 길이 차이

result = math.inf
for i in range(gap+1):
    tmp = 0
    for j in range(a_len):
        if a[j] != b[i+j]:
            tmp += 1

    if result > tmp:  # result 값 업데이트
        result = tmp

print(result)
