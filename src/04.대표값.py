# round()함수 - 소수 첫째에서 반올림
'''
python에서 round는 round_half_even 방식을 택함
    정확한 가운데 값을 가까운 짝수수로 올림//내림해버리는

a=4.500
round(a) -> 4가 나옴

a= 5.5
round(a) -> 6로 나옴(정확히 가운데 수가 아니니), 5에 쏠려있으니)


a= 4.51
round(a) -> 5로 나옴(정확히 가운데 수가 아니니), 5에 쏠려있으니)
'''

'''
반올림은 이렇게 처리
a = 66.5
a = a + 0.5
a = int(a)
'''


import sys

sys.stdin = open("input.txt","r")

N = int(input())
lst = list(map(int,input().split()))

avg = round(sum(lst)/N)

min = float('inf')

for idx, x in enumerate(lst):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        score_idx = idx +1

    elif tmp == min:
        if x > score:
            score = x
            score_idx = idx +1

# print(avg, score_idx)