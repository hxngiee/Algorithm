a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b) # 합집합
'''{1, 2, 3, 4, 5, 6, 7}'''
print(a&b) # 교집합
'''{3, 4, 5}'''
print(a-b) # 차집합
'''{1, 2}'''



# 집합 자료형 함수 모두 O(1)
data = set([1,2,3])

## add() : 새로운 원소 추가
data.add(4)
'''{1, 2, 3, 4}'''

## update() : 새로운 원소 여러 개 추가
data.update([5,6])
'''{1, 2, 3, 4, 5, 6}'''

## remove() : 특정한 값을 갖는 원소 삭제
data.remove(3)
'''{1, 2, 4, 5, 6}'''