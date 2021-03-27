# import sys
#
# sys.stdin = open('input.txt','r')
#
# INF = int(1e9)
#
# n, m, s = map(int,input().split())
#
# graph = [[INF] *(n+1) for _ in range(n+1)]
#
# for a in range(n+1):
#     for b in range(n+1):
#         if a==b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a, b, c = map(int,input().split())
#     graph[a][b] = c
#
# for x in graph:
#     print(x)
#
# print()
#
# cnt = 0
# res = []
# for i in range(n+1):
#     if graph[s][i] == INF or graph[s][i] == 0:
#         continue
#     else:
#         res.append(graph[s][i])
#         cnt += 1
#
# print(cnt, max(res))


## 해설
import heapq
import sys

sys.stdin = open('input.txt','r')
INF = int(1e9)

n, m, start = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

cnt = 0
max_distance = 0

for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance,d)

print(cnt-1, max_distance)