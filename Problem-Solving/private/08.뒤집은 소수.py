
import sys

sys.stdin = open("input.txt","r")

N = int(input())
lst = list(map(int,input().split()))


def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):  # 자연수의 절반까지만 봐도 소수 검증이 가능. 그 안에 나눠떨어지는게 없으면 됨
        if x%i==0:
            return False
    else:
        return True

for x in lst:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')