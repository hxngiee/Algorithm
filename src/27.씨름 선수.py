import sys

sys.stdin = open('input.txt','r')

n = int(input())

lst = []
for i in range(n):
    s, e = map(int,input().split())
    lst.append((s,e))
lst.sort(reverse=True)
# print(lst)

largest = 0
cnt = 0

for x,y in lst:
    # x가 키, y가 몸무게
    if y > largest:
        largest = y
        cnt += 1
print(cnt)
