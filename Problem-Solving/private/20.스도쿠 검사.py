import sys

sys.stdin = open('input.txt','r')

a = [list(map(int, input().split())) for _ in range(9)]


# 총 3가지 조건을 확인해야 함(행, 열, 그룹)
def check(a):
    for i in range(9):
        ch1 = [0] * 10      # 행 확인
        ch2 = [0] * 10      # 열 확인
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    # 그룹 탐색
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True

if check(a):
    print("Yes")
else:
    print("No")
