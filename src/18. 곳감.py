import sys

sys.stdin = open('input.txt','r')

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    idx, d, k = map(int, input().split())

    if d == 0:
        for _ in range(k):
            a[idx-1].append(a[idx-1].pop(0))     # .pop(0) : 0번 인덱스인 제일 앞꺼 빼겠다는거
    else:
        for _ in range(k):
            a[idx-1].insert(0,a[idx-1].pop())   # .insert(0,) : 0번 자리에 집어 넣으라는 뜻
                                                # .pop() : 제일 뒤에꺼 꺼냄


# 모래시계 합 만들기
res = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]
    if i<n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)