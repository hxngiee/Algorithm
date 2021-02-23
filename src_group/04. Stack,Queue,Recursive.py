## Stack : 선입후출
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# print(stack)
# print(stack[::-1])


## Queue

# Queue 구현을 위해 deque 라이브러리 사용 : Stack과 Queue의 기능을 한번에

# deque관련 method
# appendleft(),insert(), extend(),extendleft(),
# popleft(), remove(), reverse()
# https://dongdongfather.tistory.com/72

# 일부 method는 일반 list에서 사용 불가(appendleft,popleft)
# pop : 맨 오른쪽 제거, list, queue 둘다 사용가능
# popleft() : 맨 왼쪽 제거, deque 자료구조에서 사용 가능

from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)     # 먼저 들어온 순서대로 출력
queue.reverse()  # 다음 출력을 위해 역순으로 바꾸기
print(queue)     # 나중에 들어온 원소대로 출력


## 재귀함수
def factorial(n):
    if n<=1:
        return 1

    return n * factorial(n-1)

print(factorial(5))