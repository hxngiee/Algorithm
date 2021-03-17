alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# 12 -> M
# -12 -> O

# print(ord('J')-ord('A'))
# print(ord('M')-ord('A'))
# print(ord('O')-ord('A'))

# print(ord('Z')-ord('A'))

# name = 'JAZ'
# name = 'JEROEN'
# name = 'AAA'
# name = 'ZZZ'
name = 'M'
# flag = False
answer = 0


for i in range(len(name)):
    for j in range(len(alpha)):
        if name[i] == alpha[j]:
            tmp = ord(alpha[j]) - ord('A')
            if tmp > 13:
                tmp = 26 - tmp
                # flag = True
            print(tmp)
            # print(flag)
            answer += tmp
    # if name[i]=='A'or flag==True:
    if name[i]=='A':
        # flag=False
        continue
    elif i!=len(name)-1:
        print('move!!!')
        answer+=1

print(answer)

