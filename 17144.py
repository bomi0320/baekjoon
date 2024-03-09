# 미세먼지 안녕!
import sys
import math

x_direction = [0, 1, 0, -1]
y_direction = [-1, 0, 1, 0]

# 입력
r, c, t = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, sys.stdin.readline().split())))


air_cleaner = []   # 공기청정기 위치 저장해두는 리스트

for i in range(t):
    # 확산
    next_board = [[0 for _ in range(c)] for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if i == 0 and board[x][y] == -1:  # 공기청정기 위치 저장
                air_cleaner.append((x, y))
            if board[x][y] > 0:
                spread_start = board[x][y]  # 확산이 시작되는 점
                spread_amount = math.floor(spread_start/5)  # 확산되는 양
                cnt = 0  # 확산된 방향의 개수
                for k in range(4):
                    target_x = x + x_direction[k]
                    target_y = y + y_direction[k]
                    if target_x < 0 or target_x >= r or target_y < 0 or target_y >= c:
                        continue
                    if board[target_x][target_y] == -1:
                        continue
                    next_board[target_x][target_y] += spread_amount
                    cnt += 1
                next_board[x][y] += spread_start - cnt * spread_amount  # (r, c)에 남은 미세먼지의 양


    # 공기청정기
    up_start = air_cleaner[0]
    down_start = air_cleaner[1]

    # 위쪽 공기청정기(오, 위, 왼, 아래 순)
    start_x, start_y = up_start[0], up_start[1]
    next_board[start_x][start_y] = -1

    last = next_board[start_x][1]
    next_board[start_x][1] = 0

    for j in range(2, c):  # 오른쪽으로
        now = next_board[start_x][j]
        next_board[start_x][j] = last
        last = now

    for i in range(start_x-1, -1, -1):  # 위쪽으로
        now = next_board[i][c-1]
        next_board[i][c-1] = last
        last = now

    for j in range(c-2, -1, -1):  # 왼쪽으로
        now = next_board[0][j]
        next_board[0][j] = last
        last = now

    for i in range(1, start_x+1):   # 아래쪽으로
        now = next_board[i][0]
        next_board[i][0] = last
        last = now

    next_board[start_x][start_y] = -1  # 공기청정기로 들어간 미세먼지는 모두 정화된다.

    # 아래쪽 공기청정기(오, 아래, 왼, 위 순)
    start_x, start_y = down_start[0], down_start[1]

    last = next_board[start_x][1]
    next_board[start_x][1] = 0

    for j in range(2, c):  # 오른쪽으로
        now = next_board[start_x][j]
        next_board[start_x][j] = last
        last = now

    for i in range(start_x + 1, r):  # 아래쪽으로
        now = next_board[i][c-1]
        next_board[i][c-1] = last
        last = now

    for j in range(c - 2, -1, -1):  # 왼쪽으로
        now = next_board[r-1][j]
        next_board[r-1][j] = last
        last = now

    for i in range(r - 2, start_x-1, -1):  # 위쪽으로
        now = next_board[i][0]
        next_board[i][0] = last
        last = now

    next_board[start_x][start_y] = -1  # 공기청정기로 들어간 미세먼지는 모두 정화된다.

    # next_board -> board
    for i in range(r):
        for j in range(c):
            board[i][j] = next_board[i][j]


# 미세먼지의 양 계산
result = 0
for i in range(r):
    for j in range(c):
        if board[i][j] > 0:
            result += board[i][j]

print(result)
