# 이미 정렬된 두 데이터를 합할 때
# (sort()를 사용할 경우 nlogn인데 정렬된 두 리스트를 합할땐 n으로 해결할 수 있다)
# 포인터 활용하기

import sys

sys.stdin = open("input.txt","r")

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

# 포인트 변수 초기화
p1=p2=0
c = []

while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

# slice(남은거 끝까지 다 전달)
# a 리스트의 숫자가 남았을 때
if p1<n:
    c = c + a[p1:]
if p2<m:
    c = c + b[p2:]


# 원소로 출력하고 싶을 때
for x in c:
    print(x, end=' ')