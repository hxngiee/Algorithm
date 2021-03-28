import sys

sys.stdin = open('input.txt', 'r')

v, m = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
        union_parent(parent, b, c)

    elif a == 1:
        b = find_parent(parent, b)
        c = find_parent(parent, c)
        if b == c:
            print('YES')
        else:
            print('NO')


## 해설
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print('Yes')
        else:
            print('No')