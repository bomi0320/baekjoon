# 1로 만들기 2
def make_one(n):
    count = [0]*(n+1)
    method = [0]*(n+1)
    for i in range(2, n+1):
        tmp_count = [count[i - 1] + 1]
        tmp_method = [1]
        if i % 2 == 0:
            tmp_count.append(count[i // 2] + 1)
            tmp_method.append(2)
        if i % 3 == 0:
            tmp_count.append(count[i // 3] + 1)
            tmp_method.append(3)
        min_val = min(tmp_count)
        min_index = tmp_count.index(min_val)

        count[i] = min_val
        method[i] = tmp_method[min_index]

    # 출력
    print(count[n])

    while n != 1:
        print(n, end=" ")
        if method[n] == 1:
            n -= 1
        elif method[n] == 2:
            n //= 2
        else:
            n //= 3
    print(1)


n = int(input())
make_one(n)
