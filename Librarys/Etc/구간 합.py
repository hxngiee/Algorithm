# 특정 구간의 모든 수를 합한 값

# N: 데이터의 수
# M: 쿼리의 수

# M개의 쿼리 각각, 매번 구간 합을 계산한다면: O(NM)
# M개의 쿼리가 수행될때마다 전체 리스트 구간 합을 모두 계산할 수 있기 때문

# 여러 번 사용될만한 정보는 미리 저장해두자!
# Prefix Sum: 리스트의 맨 앞부터 특정 위치까지의 합
# N개의 수의 위치 각각에 대하여 접두사 합을 미리 구해 놓으면 된다

n = 5
array = [10,20,30,40,50]

# Prefix Sum 배열 계산
sum_value = 0
prefix_sum = [0]
for i in array:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(3번째 수부터 4번째 수까지)
left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1])