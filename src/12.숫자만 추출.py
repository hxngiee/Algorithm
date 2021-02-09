import sys

sys.stdin = open("input.txt","r")

s = input()

res = 0

# .isdecimal() -> 0부터 9까지 숫자만 확인
# .isdigit -> 숫자형태 다 찾음
for x in s:
    if x.isdecimal():
        res = res*10+int(x)

cnt = 0

for i in range(1, res+1):
    if res%i ==0:
        cnt += 1