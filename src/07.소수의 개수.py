import sys
sys.stdin = open('input.txt','r')

N = int(input())

# lst 0으로 다 초기화
ch = [0]*(N+1)
cnt = 0

for i in range(2,N+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i,N+1,i):    # i의 배수로 돈다!
            ch[j] = 1

# 배수가 될 놈은 1로 마킹해서 카운트 안하고

# 소수인 놈만 카운팅 하겠다

