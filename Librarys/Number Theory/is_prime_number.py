# 범위 안에 존재하는 모든 소수
# 에라토스테네의 체
import math

n = 1000 # 2부터 1000까지 모든 수에 대해 소수 판별
array = [True for i in range(n+1)] # 처음엔 모든 수가 소수인 것으로 초개화(0과 1 제외))

for i in range(2,int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(2,n+1):
    if array[i]:
        print(i, end=' ')



# 하나의 수에 대해
import math
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

'''
print(is_prime_number(4))
False

print(is_prime_number(7))
True
'''
