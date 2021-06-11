# O(NlonN)
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소 heap에 삽입
    for value in iterable:
        heapq.heappush(h,value)
        # heapq.heappusH(h,-value) # 최대 힙

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        # result.append(-heapq.heappop(h)) # 최대힙

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
'''[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'''