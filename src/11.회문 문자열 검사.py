import sys

sys.stdin = open("input.txt","r")

N = int(input())

for i in range(N):
    # 대소문자 같게 비교하기 위해 모두 대문자로 바꿔버림
    s = input()
    s = s.upper()
    size = len(s)

    for j in range(size//2):
        # 마지막부터 접근하고 싶을때 s[-1-j]
        if s[j] != s[-1-j]:
            print("#%d No"%(i+1))
            break
    else:
        print("#%d Yes"%(i+1))


# 다른 풀이 -> 문자열 reverse하기
# [python slice]
# test[::] # 리스트 전체를 가져옴
# test[::2] # 리스트 전체에서 인덱스 0부터 2씩 증가하면서 요소를 가져옴
# test[::-1] # 리스트 전체에서 인덱스를 1씩 감소시키면서 요소를 가져옴(리스트를 반대로 뒤집음)
# test[7::2] # 인덱스 7부터 2씩 증가시키면서 리스트 마지막 요소까지 가져옴
# test[5:1:-1] # 인덱스 증가폭을 음수로 지정하면, 요소를 뒤에서부터 가져올 수 있음
               # 5부터 2까지 1씩 감소시키면서 요소를 가져옴


# test = 'abcde'
# print(test[::-1])
# 맨 뒷자리부터 -1만큼 작아지면서 문자열을 거꾸로 바꿔라