# 최댓값
grid = []
for _ in range(9):
    line = list(map(int, input().split()))
    grid.append(line)

max_val = 0
index_of_max_val = [0, 0]
for i in range(9):
    for j in range(9):
        if grid[i][j] > max_val:
            max_val = grid[i][j]
            index_of_max_val[0] = i
            index_of_max_val[1] = j

print(max_val)
print(index_of_max_val[0]+1, index_of_max_val[1]+1)
