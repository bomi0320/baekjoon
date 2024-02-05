# ROT13

S = input()
for s in S:
    if s.isalpha():
        if s.isupper():  # ord('A'), ord('Z') => 65, 90
            o = ord(s) + 13
            if o > 90:
                o -= 26
            print(chr(o), end="")
        elif s.lower():  # ord('a'), ord('z') => 97, 122
            o = ord(s) + 13
            if o > 122:
                o -= 26
            print(chr(o), end="")
    else:
        print(s, end="")

