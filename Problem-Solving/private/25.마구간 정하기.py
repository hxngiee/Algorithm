import sys
import math

sys.stdin = open('input.txt','r')

def Count(len):
    # 첫번째 말 배치
    cnt = 1
    ep = lst[0]
    for i in range(1,N):
        if lst[i] - ep >= len:  # 말을 배치할 수 있는 조건
            cnt += 1
            ep = lst[i]
    return cnt

N, M = map(int, input().split())

lst = list(int(input()) for _ in range(N))
lst.sort()
print(lst)

# 두 말 사이간 최소 거리
lt = 1
rt = lst[N-1]

while lt <= rt:
    mid = (lt+rt) // 2

    # 답이 될 수 있는 것들들
    if Count(mid) >= M:
       res = mid
       lt = mid+1
    else:
        # 될 수 없는 것들
        rt = mid - 1

print(res)

