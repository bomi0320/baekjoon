# 센서

n = int(input())  # 센서의 개수
k = int(input())  # 집중국의 개수
sensors = list(map(int, input().split()))  # 센서의 위치

if n <= k:
    print(0)
else:
    sensors.sort()

    distance = []
    for i in range(1, n):
        distance.append(sensors[i] - sensors[i-1])

    distance.sort(reverse=True)

    for i in range(k-1):
        distance.pop(0)

    print(sum(distance))
