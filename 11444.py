# 피보나치 수 6
def matrix(a1, a2):
    result = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a1[i][k] * a2[k][j] % 1000000007
    return result


p_memo = {}


def p(F, n):
    y = 1
    if n == 1:
        return F
    elif n % 2 == 1:  # n이 홀수
        y = p(F, n - 1)
        return matrix(F, y)
    else:  # n이 짝수
        y = p(F, n // 2)
        return matrix(y, y)


F = [[1, 1], [1, 0]]
n = int(input())
print(p(F, n)[0][1] % 1000000007)
