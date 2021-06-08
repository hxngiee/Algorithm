import sys

sys.stdin = open('input.txt','r')

n, m = map(int,input().split())
lst = list(map(int,input().split()))

# cnt = 0
#
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] == lst[j]:
#             continue
#         cnt += 1
#
#  print(cnt)

## 해설

array = [0] * 11 # 무게 1부터 10까지 담을 수 있는 리스트

for x in lst:
    array[x] += 1

res = 0
for i in range(1,m+1):
    n -= array[i]       # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    res += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(res)