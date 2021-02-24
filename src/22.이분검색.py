import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

lst = list(map(int,input().split()))
lst.sort()

lt = 0
rt = N-1

# while문 조건 !
while lt<=rt:
    mid = (lt + rt) // 2

    if lst[mid] == M:
        print(mid + 1)
        break

    elif lst[mid] > M:
        rt = mid - 1

    elif lst[mid] < M:
        lt = mid + 1

