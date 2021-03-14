import sys
from collections import deque

sys.stdin = open('input.txt','r')
n = int(input())
lst = list(map(int,input().split()))
lt = 0
rt = n-1
last = 0

res = ""

tmp = []

while lt<=rt:
    if lst[lt] > last:
        tmp.append((lst[lt],'L'))
    if lst[rt] > last:
        tmp.append((lst[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]      # 문자열은 `+` 하면 붙음
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()                    # list 비우기
print(len(res))
print(res)