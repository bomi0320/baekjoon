# 요세푸스 문제
N, K = map(int, input().split())
num_list = [x for x in range(1, N+1)]
index = 0
result = []

for _ in range(N):
    index += K - 1
    l = len(num_list)
    if l <= index:
        index %= l
    result.append(str(num_list.pop(index)))

print("<" + ", ".join(result) + ">")
