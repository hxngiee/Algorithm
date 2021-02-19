# N = int(input())

cnt = 0
lst = []
for k in range(60):
    if k % 10 == 3:
        lst.append(k)
    elif k // 3 >= 10 and k // 3 < 13:
        lst.append(k)
    elif k == 39:
        lst.append(k)
print(lst)



# cnt = 0
# for i in range(6):
#     if i%10 == 3:
#         cnt+=1
#     for j in range(60):
#         if j%10 == 3:
#             cnt+=1
#         elif j//3>=10 and k//3<=13:
#             cnt+=1
#         for k in range(60):
#             if k%10 == 3:
#                 cnt += 1
#             elif k//3 >= 10 and k//3 <=13:
#                 cnt += 1
#
# print('%d:%d:%d'%(i,j,k))
# print(cnt+18)
