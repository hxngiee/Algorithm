N = int(input())

lst = [list([0]*N) for j in range(N)]

x = y = 0

lst[x][y] = 1

cnt = 0

while cnt < N:
    dir = input()

    if dir == 'R':
        for i in range(N-1):
            if lst[i][N-1] == 1:
                break
        else:
            lst[x][y] = 0
            lst[x][y+1] = 1
            y += 1
            cnt += 1

    if dir == 'U':
        for i in range(N-1):
            if lst[0][i] == 1:
                break
        else:
            lst[x][y] = 0
            lst[x-1][y] = 1
            x -= 1
            cnt += 1

    if dir == 'D':
        for i in range(N-1):
            if lst[N-1][i] == 1:
                break
        else:
            lst[x][y] = 0
            lst[x+1][y] = 1
            x += 1
            cnt += 1

    if dir == 'L':
        for i in range(N-1):
            if lst[i][0] == 1:
                break
        else:
            lst[x][y] = 0
            lst[x][y-1] = 1
            y -= 1
            cnt += 1

    for t in lst:
        print(t)
print(x+1,y+1)