import sys

sys.stdin = open('input.txt','r')
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

for i in range(m):
    if b[i] in a:
        print('yes')
    else:
        print('no')

## 시간복잡도 이해하신분 ?
## 문제 해설 풀이 공부
## 이진 탐색
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for x in b:
    result = binary_search(a,x,0,n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no', end=' ')



# set 활용, 더 간결
# a = set(a)
# for x in b:
#     if x in a:
#         print('yes')
#     else:
#         print('no')
