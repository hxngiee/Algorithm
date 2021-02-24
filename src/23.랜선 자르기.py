# 답의 범위가 1 ~ 802 사이에 있음

import sys

sys.stdin = open('input.txt', 'r')


def Count(len):
    cnt = 0
    for x in lst:
        cnt += (x // len)
    return cnt


N, M = map(int, input().split())
lst = []
res = 0
for _ in range(N):
    lst.append(int(input()))

max = max(lst)

lt = 1
rt = max

while lt <= rt:
    # 최대의 mid를 구하는 방법
    mid = (lt + rt) // 2

    # 길이가 짧을 때
    if Count(mid) >= M:
        res = mid
        lt = mid + 1  # 더 좋은 수(큰 수)를 향해 찾아 나가야함
    else:
        # 길이가 길때
        rt = mid - 1

print(res)
