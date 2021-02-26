# N, M = 3, 3
N, M = 2, 4
# lst = [[3,1,2],[4,1,4],[2,2,2]]
lst = [[7,3,1,8],[3,3,3,4]]

res = []

for i in range(N):
    res.append(min(lst[i][:]))

print(max(res))