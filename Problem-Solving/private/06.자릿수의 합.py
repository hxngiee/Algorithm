import sys

sys.stdin = open('input.txt','r')

N = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum+=x%10
        x = x//10
    return sum

max = float('-inf')

# 리스트 이렇게 호출하면 값 바로 불러옴
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

## 다른 테크닉
def digit_sum(x):
    sum = 0

    # 이러면 전체 수를 가져와서 하나씩 읽어 들여 연산 가능
    for i in str(x):
        sum += int(i)

    return sum