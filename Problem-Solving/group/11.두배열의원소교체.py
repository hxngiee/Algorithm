import sys

sys.stdin = open('input.txt','r')

n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

# for i in range(k):
#     swp_a = min(a)
#     swp_b = max(b)
#
#     a.remove(swp_a)
#     b.remove(swp_b)
#
#     a.append(swp_b)
#     b.append(swp_a)
#
# print(sum(a))


## sol
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]     # 이렇게 하면 바로 swap할 수 있구나
    else:
        break

print(sum(a))