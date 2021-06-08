import sys

sys.stdin = open('input.txt', 'r')
lst = list(input())
print(lst)

# zero = 0
# one = 0
#
# cnt = 0
# flag = False
#
# tmp = lst[0]
# if int(tmp) == 0:
#     zero += 1
# else:
#     one += 1
#
# for i in range(1, len(lst)):
#     if tmp == lst[i]:
#         flag = True
#     else:
#         flag = False
#
#     # print(flag)
#
#     if not flag:
#         if int(lst[i]) == 0:
#             zero += 1
#         else:
#             one += 1
#
#     tmp = lst[i]
#
# print(min(zero,one))

## sol
count0 = 0
count1 = 0

if lst[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 확인
for i in range(len(lst) - 1):
    if lst[i] != lst[i + 1]:

        # 다음 수에서 1로 바뀌는 경우
        if lst[i + 1] == '1':
            count0 += 1

        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))