# 8진수 2진수

octal = input()
decimal = int(octal, base=8)
binary = bin(decimal)
print(binary[2:])
