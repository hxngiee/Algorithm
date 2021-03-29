import sys

sys.stdin = open('input.txt','r')
v, e = map(int,input().split())

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i

edges = []
res = 0
tmp = [] # last = 0

for i in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        res += cost
        tmp.append((cost,a,b)) # last=cost
        # print("a: %d b: %d, cost: %d"%(a,b,cost))

print(res-tmp[-1][0]) # res-last