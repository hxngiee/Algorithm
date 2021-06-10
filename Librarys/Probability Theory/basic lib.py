# 모든 경우의 수를 고려하는데 활용됨

## 순열 : 서로 다른 r개를 선택하여 일렬로 나열(순서가 중요)
from itertools import permutations
data = ['A','B','C'] #데이터 준비
result = list(permutations(data,3)) # 모든 순열 구하기
'''[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]'''

## 조합 : 순서에 상관없이 서로 다른 r개를 선택하는 것
from itertools import combinations
data = ['A','B','C'] # 데이터 준비
result = list(combinations(data,2)) # 2개 뽑는 모든 조합 구하기
'''[('A', 'B'), ('A', 'C'), ('B', 'C')]'''

## 중복 순열
from itertools import product
data = ['A','B','C'] # 데이터 준비
result = list(product(data,repeat=2)) # 2개 뽑는 모든 순열 구하기
'''[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]'''

## 중복 조합
from itertools import combinations_with_replacement
data = ['A','B','C'] # 데이터 준비
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용))
'''[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]'''
