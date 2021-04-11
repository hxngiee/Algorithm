n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2,length):
    summary -= int(n[1])

if summary == 0:
    print('LUCKY')
else:
    print('READY')