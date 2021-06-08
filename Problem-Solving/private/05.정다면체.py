import sys

sys.stdin = open("input.txt","r")

N, M = map(int,input().split())

# 리스트 0으로 초기화, +3만큼 넉넉히 잡음
cnt = [0]*(N+M+3)

max = 0

for i in range(1,N+1):
    for j in range(1,M+1):
        cnt[i+j] += 1

for i in range(N+M+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(N+M+1):
    if max == cnt[i]:
        print(i, end=' ')