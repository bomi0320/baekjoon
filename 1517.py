# 버블 소트
result = 0


def merge_sort(start, end):
    global result

    if end - start < 1:
        return
    mid = start + (end - start) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)

    # merge
    for i in range(start, end + 1):
        tmp[i] = A[i]
    k = start
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if tmp[i] <= tmp[j]:
            A[k] = tmp[i]
            k += 1
            i += 1
        else:
            A[k] = tmp[j]
            result += j - k
            k += 1
            j += 1

    # 남아 있는 것들 정리
    while i <= mid:
        A[k] = tmp[i]
        k += 1
        i += 1
    while j <= end:
        A[k] = tmp[j]
        k += 1
        j += 1


N = int(input())
A = list(map(int, input().split()))
tmp = [0] * (N + 1)
merge_sort(0, N-1)
print(result)
