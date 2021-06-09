# 접근할 데이터 범위 표현
# 2개의 변수를 이용해 리스트상 위치 기록


## 특정한 합을 가지는 부분 연속 수열 찾기
n = 5 # 데이터 개수
m = 5 # 찾고자 하는 부분 합
array = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시켜 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += array[end]
        end += 1

    if interval_sum == m:
        count += 1
    interval_sum -= array[start]

print(count)



## 정렬되어 있는 두 리스트의 합집합
# 단순히 각 리스트의 모든 원소를 한 번씩만 순회하면 되기 때문에 O(N+M)
# Merge Sort

n,m = 3,4 # 두 리스트의 원소 개수
a = [1,3,5]
b = [2,4,6,8]

# 리스트 a,b를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n + m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i<n or j<m:
    # 리스트 b의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j>=m or (i<n and a[i]<=b[j]):
        result[k] = a[i]
        i += 1
    # 리스트 a의 모든 원소가 처리되었거나,, 리스트 B의 원소가 더 작을 때
    else:
        result[k] = b[j]
        j += 1
    k += 1

# for i in result:
#     print(i,end=' ')
