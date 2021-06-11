from collections import deque
# deque에서는 list와 다르게 인덱싱, 슬라이싱을 사용할 수 없음
# 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입/삭제시 효율적

''' list / deque
가장 앞쪽 원소 추가 : O(N) / O(1)
가장 뒤쪽 원소 추가 : O(1) / O(1)
가장 앞쪽 원소 제거 : O(N) / O(1)
가장 뒤쪽 원소 제거 : O(1) / O(1)
'''

array = deque([2,3,4])

array.appendleft(1)
'''[1,2,3,4]'''

array.popleft()
'''[2,3,4]'''