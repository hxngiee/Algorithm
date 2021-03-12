import sys

sys.stdin = open('input.txt','r')
n = int(input())

# 가능한 opt 중 1까지 갔을 때 cnt가 가장 적은 것 선택

def Cnt(a):
    if a==1:
        return 0

    if a%5 ==0:
        return 1 + Cnt(a//5)
    elif a%3 == 0:
        return 1 + Cnt(a // 3)
    elif a%2 ==0:
        return 1 + Cnt(a//2)
    else:
        return 1 + Cnt(a-1)

print(Cnt(26))
