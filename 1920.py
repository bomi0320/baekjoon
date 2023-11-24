# 수 찾기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

A.sort()


def find(start, end, data):
    middle = (start+end)//2

    if start > end:  # 데이터가 존재하지 않는 경우
        return 0

    if A[middle] == data:
        return 1
    if A[middle] > data:
        return find(start, middle - 1, data)
    else:
        return find(middle + 1, end, data)


for t in target:
    print(find(0, N-1, t))
