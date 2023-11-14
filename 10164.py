# 격자상의 경로

def num_of_route(n, m, k):
    grid = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # base case
    for i in range(1, n+1):
        grid[i][1] = 1
    for i in range(1, m+1):
        grid[1][i] = 1

    if k == 0:
        # 채우기
        for i in range(2, n+1):
            for j in range(2, m+1):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    else:  # k를 무조건 지나가야 함
        # k 인덱스 구하기
        x = (k-1) // m+1
        y = k % m
        if y == 0:
            y = m

        # k까지 채우기
        for i in range(2, x+1):
            for j in range(2, y+1):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        # base case
        for i in range(x+1, n+1):
            for j in range(0, y):
                grid[i][j] = 0
        for i in range(0, x):
            for j in range(y+1, m+1):
                grid[i][j] = 0

        # 나머지 채우기

        for i in range(x, n+1):
            for j in range(y, m+1):
                if i == x and j == y:
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    print(grid[n][m])


n, m, k = map(int, input().split())

if n == 1 or m == 1:
    print(1)
else:
    num_of_route(n, m, k)
