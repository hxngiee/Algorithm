import sys

sys.stdin = open("input.txt","r")

a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        # 이런식으로 값을 간단하게 Swap해줄 수 있음
        a[s+i], a[e-i] = a[e-i], a[s+i]

print(len(a))
# 맨 앞에 편의를 위해 만들어 놓은 수 제거
a.pop(0)
for x in a:
    print(x, end=' ')