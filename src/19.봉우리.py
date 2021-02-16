import sys

sys.stdin = open('input.txt','r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

# 가장자리 초기화
a.insert(0,[0]*n)   # 맨위 : 0번 index에 [0]*n을 추가
a.append([0]*n)     # 맨아래


for x in a:
    x.insert(0,0)
    x.append(0)

cnt = 0

# 봉우리 판단
# all()은 안에 내용이 모두 참일 때, 참을 반환
for i in range(1, n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            # k가 0부터 4까지 돔
            cnt += 1

print(cnt)
