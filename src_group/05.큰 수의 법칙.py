# N, M, K = 5, 8, 3
N, M, K = 5, 7, 2

# lst = [2,4,5,4,6]
lst = [3,4,3,4,3]
lst.sort()

rt = N-1

cnt = 0
sum = 0
for i in range(M):
    sum += lst[rt]
    cnt += 1
    # print(lst[rt])
    # print(cnt)

    if cnt == K :
        # print('-' * 30)
        rt -= 1
        cnt = 0
    elif rt != N-1:
        rt += 1

print(sum)
