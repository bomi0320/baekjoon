result = 0


def f(s):
  global result
  l = len(string)
  alpha = [s[0]]
  for i in range(1, l):
    if s[i] == s[i - 1]:
      continue
    elif s[i] in alpha:
      return
    else:
      alpha.append(s[i])
  result += 1


t = int(input())
for _ in range(t):
  string = input()
  f(string)
print(result)
