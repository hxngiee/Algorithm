import sys

sys.stdin = open('input.txt','r')

a = [list(map(int,input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        # 가로 확인
        # slice
        tmp = a[j][i:i+5]
        # 역순
        if tmp == tmp[::-1]:
            cnt += 1

        # 세로 확인
        for k in range(2):
            if a[i+k][j] != a[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)