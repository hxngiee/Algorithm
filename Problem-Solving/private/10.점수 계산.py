import sys

sys.stdin = open("input.txt","r")

N = input()

lst = list(map(int,input().split()))

sum = 0
cnt = 0
for i in lst:
    if i:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)