from collections import deque
import sys

sys.stdin = open('input.txt','r')
v = int(input())

indegree = [0] * (v+1)
cost = [0] * (v+1)
graph = [[] for i in range(v+1)]

flag = True

for i in range(1,v+1):
    lst = deque(list(map(int,input().split())))

    while lst:
        now = lst.popleft()
        if now == -1:
            flag=True
            break

        if flag:
            cost[i] = now
            flag = False
            continue

        graph[now].append(i)
        indegree[i] += 1

# print(cost)
# print(graph)
# print(indegree)

res = [0] * (v+1)

def topology_sort():
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        res[now] += cost[now]

        for i in graph[now]:
            res[i] = 0
            res[i] += res[now]
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

topology_sort()

print(res)
