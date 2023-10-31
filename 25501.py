# 재귀의 귀재

def recursion(s, l, r):
  global numOfRecursionCall
  if l >= r:
    return 1
  elif s[l] != s[r]:
    return 0
  else:
    numOfRecursionCall += 1
    return recursion(s, l + 1, r - 1)


def isPalindrome(s):
  return recursion(s, 0, len(s) - 1)


t = int(input())
for _ in range(t):
  s = input()
  numOfRecursionCall = 1
  print(isPalindrome(s), numOfRecursionCall)
