# 회의실 하나에서 최대한 회의를 많이 해야함으로 회의가 끝나는 시간을 기준으로 정렬
# 2 3
# 1 4
# 3 5
# 4 6
# 5 7

import sys

sys.stdin = open('input.txt','r')

N = int(input())

lst = []
for i in range(N):
    s, e = map(int, input().split())

    # 시작, 끝 시간을 튜플 형태로 넣음
    lst.append((s,e))
lst.sort(key=lambda x : (x[1], x[0]))   # 정렬순위를 정해주는 것

et = 0
cnt = 0
for s,e in lst:
    if s >= et:
        et = e
        cnt += 1
print(cnt)