# 자주 사용되는 내장 함수

# sum
result = sum([1,2,3,4,5])
print(result)

# min, max
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result, max_result)

# eval() : 사람의 입장에서 표현된 하나의 수식을 실제 수의 형태로 반환
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4],reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동',35), ('이순신',75), ('아무개',50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 순열과 조합
## 모든 경우의 수를 고려하는데 활용됨

## 순열 : 서로 다른 r개를 선택하여 일렬로 나열(순서가 중요)
from itertools import permutations
data = ['A','B','C'] #데이터 준비
result = list(permutations(data,3)) # 모든 순열 구하기
print(result)

## 조합 : 순서에 상관없이 서로 다른 r개를 선택하는 것
from itertools import combinations
data = ['A','B','C'] # 데이터 준비
result = list(combinations(data,2)) # 2개 뽑는 모든 조합 구하기
print(result)

## 중복 순열
from itertools import product
data = ['A','B','C'] # 데이터 준비
result = list(product(data,repeat=2)) # 2개 뽑는 모든 순열 구하기
print(result)

## 중복 조합
from itertools import combinations_with_replacement
data = ['A','B','C'] # 데이터 준비
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용))
print(result)


# Counter
## 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능 제공
## 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter)) # 사전(dictionary) 자료형으로 반환


# 최대 공약수와 최소 공배수
## 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수를 이용할 수 있음
import math
def lcm(a,b):
    return a*b // math.gcd(a,b)
a = 21
b = 14
print(math.gcd(21,14)) # 최대 공약수(GCD: 공통된 약수중 가장 큰 값) 계산
print(lcm(21,14)) # 최소 공배수(LCM: 공통된 배수중 가장 작은 값) 계산