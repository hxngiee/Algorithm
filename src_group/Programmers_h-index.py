# lst = [3,0,6,1,5]
# lst = [0,0,0,0,0]
lst = [10, 50, 100]

n = len(lst)

cnt = 0

h_lst = []

for i in range(len(lst)+1):
    # h = lst[i]

    for j in range(len(lst)):
        if lst[j] >= i:
            cnt += 1

    if cnt >= i:
        h_lst.append(i)
    cnt = 0

# print(h_lst)
print(max(h_lst))
