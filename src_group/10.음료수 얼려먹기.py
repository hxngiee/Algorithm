import sys

sys.stdin = open('input.txt','r')

n, m = map(int,input().split())
# print(n,m)

lst = [list(map(int,input())) for _ in range(n)]
# for x in lst:
#     print(x)


## 반대쪽도 해줘야하네ㅠㅠㅠ

def f_row_r(i,j):
    if j+1 >=m :
        return
    if lst[i][j+1] == 1:
        return
    else:
        lst[i][j+1] = 1
        f_row_r(i,j+1)
        f_row_l(i,j+1)
        f_col_d(i,j+1)
        f_col_u(i,j+1)

def f_row_l(i,j):
    if j-1 < 0:
        return
    if lst[i][j-1] == 1:
        return
    else:
        lst[i][j-1] = 1
        f_row_r(i,j-1)
        f_row_l(i,j-1)
        f_col_d(i,j-1)
        f_col_u(i,j-1)

def f_col_d(i,j):
    if i+1 >=n:
        return
    if lst[i+1][j]==1:
        return
    else:
        lst[i+1][j] = 1
        f_col_d(i+1,j)
        f_col_u(i+1,j)
        f_row_r(i+1,j)
        f_row_l(i+1,j)

def f_col_u(i,j):
    if i-1 < 0:
        return
    if lst[i-1][j] == 1:
        return
    else:
        lst[i-1][j] = 1
        f_col_d(i-1,j)
        f_col_u(i-1,j)
        f_row_r(i-1,j)
        f_row_l(i-1,j)




cnt = 0
x = 1
y = 1

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:

            cnt += 1
            lst[i][j] = 1

            print(i,j)

            # 가로, 세로 정리 끝
            f_row_r(i,j)
            f_row_l(i,j)
            f_col_d(i,j)

print(cnt)
