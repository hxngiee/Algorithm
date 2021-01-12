import sys

sys.stdin = open("input.txt","rt")

N, K = map(int,input().split())
a = list(map(int, input().split()))

# set의 활용
# set의 인자 추가는 add임 (append 아님)
res = set()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res.add(a[i]+a[j]+a[k])

# set은 sort가 없으 list로 변환
# list의 내림차순 정렬은 .sort(reverse=True)

res = list(res)
res.sort(reverse=True)

print(res[K-1])
