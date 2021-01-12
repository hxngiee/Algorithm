# 최소값 구하기
arr = [5,3,7,9,2,5,2,6]

# 파이썬에서 가장 큰 수 초기화 법
arrMin = float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

# 이렇게 구해도 됨
# for x in arr:
#     if x <arrMin:
#         arrMin = x
