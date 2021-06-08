import sys

# sys.stdin = open("input.txt","rt")

T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(lst)

    lst = lst[s-1:e]
    lst.sort()
    print("#%d %d"%(t+1,lst[k-1]))