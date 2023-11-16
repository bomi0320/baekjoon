# 숫자 야구
import sys


n = int(input())

question = []
strike = []
ball = []
for _ in range(n):
    q, s, b = sys.stdin.readline().split()
    question.append(q)
    strike.append(int(s))
    ball.append(int(b))

result = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            p0, p1, p2 = str(a), str(b), str(c)
            if p0 == p1 or p1 == p2 or p2 == p0:
                continue

            cnt = 0
            for i in range(n):
                q0, q1, q2 = question[i][0], question[i][1], question[i][2]
                num_s, num_b = 0, 0

                if p0 == q0:
                    num_s += 1
                if p0 == q1 or p0 == q2:
                    num_b += 1

                if p1 == q1:
                    num_s += 1
                if p1 == q0 or p1 == q2:
                    num_b += 1

                if p2 == q2:
                    num_s += 1
                if p2 == q0 or p2 == q1:
                    num_b += 1

                # 맞으면
                if num_s == strike[i] and num_b == ball[i]:
                    cnt += 1
                else:
                    break

            if cnt == n:
                result += 1

print(result)
