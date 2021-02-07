import sys
sys.stdin = open("input.txt","r")

N = int(input())

res = 0

for i in range(N):
    # 띄어 쓰기로 되어있으니까 .split()하면
    # char type으로 list화됨
    tmp = input().split()

    # 정렬해서
    tmp.sort()

    # a,b,c에 숫자로 mapping
    a,b,c = map(int, tmp)
    # print(a,b,c)

    if a==b and b==c:
        money=10000 + a*1000
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money = 1000 + (b * 100)
    else:
        money = c*100

    if money > res:
        res = money

print(res)