import sys

sys.stdin = open('input.txt','r')

lst = list(input())
# print(lst)
#
# res = 0
# oper = '*'
# for x in lst:
#     if res == 0 or x==0:
#         oper = '+'
#
#     if oper == '+':
#         res += int(x)
#     else:
#         res *= int(x)
#
#     if x == '0':
#         oper = '+'
#         continue
#     else:
#         oper = '*'
#
# print(res)

## sol
result = int(lst[0])  # 첫 번째 문자를 숫자로 변경하여 대입

for i in range(1, len(lst)):
    num = int(lst[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

