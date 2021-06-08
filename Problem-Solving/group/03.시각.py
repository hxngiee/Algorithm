N = int(input())

cnt = 0
lst = []
for k in range(60):
    if k % 10 == 3:
        lst.append(k)
    elif k // 3 >= 10 and k // 3 < 13:
        lst.append(k)
    elif k == 39:
        lst.append(k)
print(lst)



cnt = 0
for i in range(N+1):
    if i in lst:
        cnt += 60*60
    else:
        for j in range(60):
            if j in lst:
                cnt += 60
            else:
                cnt += 15

print('%d:%d:%d'%(i,j,k))
print(cnt)
