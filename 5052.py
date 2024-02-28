# 전화번호 목록
import sys


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head
        for char in string:
            if char == " ":
                continue
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                if current_node.data:
                    return True
                else:
                    return False
        return True


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    phone_number = []
    for _ in range(n):
        phone_number.append(sys.stdin.readline().strip())

    trie = Trie()
    flag = True
    for i in phone_number:
        if trie.starts_with(i):
            flag = False
            break
        else:
            trie.insert(i)

    if flag:
        print("YES")
    else:
        print("NO")


