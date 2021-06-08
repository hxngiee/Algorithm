N = 3870

lst = [500,100,50,10]
lst_cnt = [0]*4

idx = 0
for x in lst:
    lst_cnt[idx] += N//x
    N = N - x *(N//x)
    idx += 1
    print(N)

print(lst_cnt)
print(sum(lst_cnt))