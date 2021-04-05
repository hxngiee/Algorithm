import sys

sys.stdin = open('input.txt','r')

n = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)

# print(lst)
#
# cnt = 0
#
# while lst:
#     tmp = lst[-1]
#
#     if lst[0] > len(lst):
#         break
#
#     for i in range(tmp):
#         rm = lst.pop()
#     cnt += 1
#
# print(cnt)

## sol
lst.sort()
result = 0 # 그룹수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in lst:
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:
        result += 1
        count = 0
print(result)

