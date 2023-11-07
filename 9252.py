# LCS 2

import sys
sys.setrecursionlimit(100000)

def lengthLCS(s, t, m, n, length_map, sub_map):
    # base case
    for i in range(m+1):
        length_map[i][0] = 0
    for i in range(n+1):
        length_map[0][i] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                length_map[i][j] = length_map[i-1][j-1] + 1
                sub_map[i][j] = 0
            else:
                length_map[i][j] = max(length_map[i][j-1], length_map[i-1][j])
                if length_map[i][j] == length_map[i][j-1]:
                    sub_map[i][j] = 1
                else:
                    sub_map[i][j] = 2

    return length_map[m][n]


def printLCS(s, t, m, n, sub_map):
    if m == 0 or n == 0:
        return
    if sub_map[m][n] == 0:  # 대각선에서 옴
        printLCS(s, t, m-1, n-1, sub_map)
        print(s[m-1], end="")
    elif sub_map[m][n] == 1:
        printLCS(s, t, m, n-1, sub_map)
    elif sub_map[m][n] == 2:
        printLCS(s, t, m-1, n, sub_map)


a = input()
b = input()
m, n = len(a), len(b)
length_map = [[0 for _ in range(n+1)] for _ in range(m+1)]
sub_map = [[0 for _ in range(n+1)] for _ in range(m+1)]

print(lengthLCS(a, b, m, n, length_map, sub_map))
printLCS(a, b, m, n, sub_map)
