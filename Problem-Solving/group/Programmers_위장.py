clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

answer = {}

from collections import Counter
cnt = Counter([kind for name, kind in clothes])
print(cnt)

res = 1
for i in cnt.values():
    res *= (i+1)
print(res-1)