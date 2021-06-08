lst = list([0 for x in range(8)] for _ in range(8))

row = 0
col =  0
cnt = 0

# 가로 1칸 위아래 2칸 (8가지)
# 가로 2칸 위아래 1칸 (8가지)
dir1 = [2,-2]
dir2 = [1,-1]

dir3 = [1,-1]
dir4 = [2,-2]

tmp_r = 0
tmp_c = 0

# 현재 위치 기준 8가지 경우 조합
for i in range(2):
    for j in range(2):
        tmp_r += dir1[i]
        tmp_c += dir2[j]

        if tmp_r < 0 or tmp_r > 7 or tmp_c < 0 or tmp_c > 7:
            print('out of index')
        else:
            cnt += 1

        tmp_r = row
        tmp_c = col

        tmp_r += dir3[i]
        tmp_c += dir4[j]

        if tmp_r < 0 or tmp_r > 7 or tmp_c < 0 or tmp_c > 7:
            print('out of index')
        else:
            cnt += 1

        tmp_r = row
        tmp_c = col

print(cnt)