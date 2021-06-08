import heapq


def solution(scoville, K):
    answer = 0
    h = []
    for num in scoville:
        heapq.heappush(h, num)
    cnt = 0
    while h[0] < K:
        try:
            heapq.heappush(h, heapq.heappop(h) + (heapq.heappop(h) * 2))
        except:
            return -1
        cnt += 1

    return cnt

