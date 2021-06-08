import sys

sys.stdin = open('input.txt','r')

n = int(input())
lst = list(map(int,input().split()))

# res_o = 0
# res_e = 0
# res = 0
#
# for i in range(0,n,2):
#     res_o += lst[i]
#
#     if n%2 == 1 and n-1 == i:
#         continue
#     else:
#         res_e += lst[i+1]
#
# if res_o >= res_e:
#     res = res_o
# else:
#     res = res_e
#
# print(res)


## 해설
# DP문제. 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# bottom up 방식의 DP
d[0] = lst[0]
d[1] = max(lst[0],lst[1])

for i in range(2,n):
    d[i] = max(d[n-1], d[i-2] + lst[i])

print(d[n-1])