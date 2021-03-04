import sys

sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

lst = list([0] * m for _ in range(n))
# print(lst)

x, y, dir = map(int, input().split())
# print(x,y,dir)

for i in range(n):
    lst[i][:] = map(int, input().split())

lst_dir = [0, 1, 2, 3]
idx = 0

ud = [-1, 0, 1, 0]
rl = [0, 1, 0, -1]

res = []

cnt = 0

while (True):
    ## 사방이 바다인 경우
    for i in range(4):
        res.append(lst[x + ud[i]][y + rl[i]])
    if all(res):
        break

    # 1은 다 가본칸으로 처리. 가본놈이면 Only Turn
    if lst[x + ud[idx]][y + rl[idx]] == 1:
        idx += 1
    else:
        # 현재 위치 가본 경로로 표시
        lst[x + ud[idx]][y + rl[idx]] = 1

        idx += 1
        x += ud[idx]
        y += rl[idx]

    # 뒤가 1이라면 just turn
    if lst[x + ud[(idx + 2) % 4]][y + rl[[(idx + 2) % 4]]] == 1:
        idx += 1
    else:
        뒤로
        한칸
        이동

    res.clear()

# step1

# step2

# step3

