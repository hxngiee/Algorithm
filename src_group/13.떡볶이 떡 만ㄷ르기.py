import sys

sys.stdin = open('input.txt','r')

n,m = map(int,input().split())

lst = list(map(int,input().split()))
lst.sort()
#
# h_max = lst[-1]
# h = 0
#
# while m>h:
#     h = 0
#
#     for x in lst:
#         if x <= h_max:
#             continue
#         else:
#             h += x - h_max
#     if h==m:
#         break
#     else:
#         h_max -= 1
#
# print(h_max)
#
#

## 해설
st = 0
end = max(lst)

result = 0
while (st<=end):
    total = 0
    mid = (st + end) // 2
    for x in lst:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid -1
    else:
        result = mid
        st = mid + 1

print(result)