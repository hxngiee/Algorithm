N, K = 25, 5

cnt = 0

while N>1:
    if N%K==0:
        N /= K
        cnt += 1
    else:
        N -= 1
        cnt += 1

print(cnt)