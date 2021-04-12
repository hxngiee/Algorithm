import sys

sys.stdin = open('input.txt','r')

data = input()

res = []
value = 0

for x in data:
    if x.isalpha():
        res.append(x)
    else:
        value += int(x)

if value != 0:
    res.append(str(value))

print(''.join(res))