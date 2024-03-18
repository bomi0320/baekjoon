# 수열

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 구하기
for i in range(1, n):
    arr[i] = arr[i-1] + arr[i]

# K일의 온도의 합이 최대가 되는 값 구하기
max_val = arr[k-1]
for i in range(k, n):
    tmp = arr[i] - arr[i-k]
    if tmp > max_val:
        max_val = tmp

print(max_val)
