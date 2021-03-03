import sys

sys.stdin = open('input.txt','r')

row = int(input())

lst = list(map(int,input().split()))

M = int(input())

# 매번 sort해서 가장 큰(맨뒤), 작은(맨앞) 것 바꿈
lst.sort()

for _ in range(M):
    lst[0] += 1
    lst[-1] -= 1
    lst.sort()

print(lst[-1]-lst[0])
