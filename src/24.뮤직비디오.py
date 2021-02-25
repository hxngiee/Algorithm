import sys

sys.stdin = open('input.txt','r')
def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum+x > capacity:
            cnt += 1    # 새로운 dvd 필요
            sum = x
        else:
            sum += x
    return cnt

N, M = map(int, input().split())

Music = list(map(int,input().split()))

lt = 1
rt = sum(Music)

res = 0

while lt<=rt:
    mid = (lt+rt)//2

    # 필요한 dvd 한장의 용량을 mid로 전달해줄 때
    # N곡을 다 저장하려면 dvd 몇장이 필요한지 return해주는 함수

    if Count(mid)<=M:
        res = mid
        rt = mid - 1
    else:
        # 용량이 너무 작아서 큰 값이 필요할 때
        lt = mid + 1
print(res)

