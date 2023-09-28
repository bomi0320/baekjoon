from itertools import combinations

heights = []
for _ in range(9):
  heights.append(int(input()))
heights.sort()

all_height = sum(heights)  # 모든 키를 더한 것

nums = [i for i in range(9)]
combi = list(combinations(nums, 2))
#print(combi)

for i in combi:
  #print(i, i[0], i[1])
  temp = heights[i[0]] + heights[i[1]]
  #print(temp)
  if all_height - temp == 100:
    del heights[i[1]]
    del heights[i[0]]
    break

for i in heights:
  print(i)
