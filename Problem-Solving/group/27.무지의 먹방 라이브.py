# food_times = [3,1,2]
#
# k = 5

# idx = 0
# for i in range(k):
#     if food_times[idx] == 0:
#         idx += 1
#         idx%=len(food_times)
#
#     food_times[idx] -= 1
#
#     idx += 1
#     idx%=len(food_times)
#
# print(idx+1)

## 해설

import heapq

def solution(food_times,k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda  x: x[1])
    return result[(k-sum_value) % length][1]
