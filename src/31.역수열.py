import sys
from collections import deque

sys.stdin = open('input.txt','r')
n = int(input())
lst = list(map(int,input().split()))

seq = [False] * n
print(seq)

for i in range(n):
    for j in range(n):
        if lst[i] == 0 and seq[j] == 0:     # 자리에 맞게 찾아간 경우
            seq[j] = i+1
            break
        elif seq[j] == 0:
            lst[i] -= 1

print(seq)

