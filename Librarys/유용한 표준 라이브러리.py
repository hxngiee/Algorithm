# 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4],reverse=True)
'''[1, 4, 5, 8, 9]
   [9, 8, 5, 4, 1]'''

# sorted() with key
array = [('홍길동',35), ('이순신',75), ('아무개',50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
'''[('이순신', 75), ('아무개', 50), ('홍길동', 35)]'''

# Counter
from collections import Counter
## 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능 제공
## 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌
counter = Counter(['red','blue','red','green','blue','blue'])
counter['blue']
'''3'''
counter['green']
'''1'''
dict(counter) # dictionary 자료형으로 반환
'''{'red'':2, 'blue':3, 'green':1}'''


# math lib
import math

## pi, e
math.pi
'''3.14 . . .'''
math.e
'''2.71 . . . '''

## factorial
math.factorial(5)
'''120'''

## sqrt : 제곱근
math.sqrt(7)
'''2.6457513110645907'''

## GCD(최대공약수): 공통된 약수중 가장 큰 값 계산
math.gcd(21,14)
'''7'''

# LCM(최소 공배수): 공통된 배수중 가장 작은 값) 계산
def lcm(a,b):
    return a*b // math.gcd(a,b)
a = 21
b = 14
'''42'''