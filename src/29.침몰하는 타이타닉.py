# list와 deque의 차이
# list는 pop하면 뒤에 수 전부 앞으로 끌어와야하나
# deque의 경우 index만 변경해서 훨씬 효율적

import sys
from collections import deque
sys.stdin = open('input.txt','r')

n, m = map(int,input().split())
lst = list(map(int,input().split()))

lst.sort()

## list2deque
lst = deque(lst)

cnt = 0

## lst가 비어있지 않으면 참이되고, 비어있으면 멈추게됨
while lst:
    if len(lst) == 1:
        cnt += 1
        break

    if lst[0] + lst[-1] > m:
        cnt += 1
        lst.pop()   # 맨 뒷수 제거
    else:
        # lst.pop(0)  # list에서 맨 앞수 제거
        lst.popleft()  # deque에서 맨 앞수 제거
        lst.pop()
        cnt += 1

print(cnt)