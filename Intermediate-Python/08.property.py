# class Natural:
#     def __init__(self,n):
#         self.setn(n)
#     def getn(self):
#         return self.__n
#     def setn(self,n):
#         if(n<1):
#             self.__n = 1
#         else:
#             self.__n = n
#     # property 객체 생성, method 등록
#     n = property(getn,setn)
#
# n1 = Natural(1)
# n2 = Natural(2)
# n3 = Natural(3)
#
# n1.n = n2.n + n3.n
# print(n1.n)



class Natural:
    def __init__(self,n):
        self.setn(n)
    n = property()
    def getn(self):
        return self.__n
    n = n.getter(getn)      # getn 메소드를 게터로 등록
    def setn(self,n):
        if (n<1):
            self.__n = 1
        else:
            self.__n = n
    n = n.setter(setn)      # setn 메소드를 세터로 등록

n1 = Natural(1)
n2 = Natural(2)
n3 = Natural(3)

n1.n = n2.n + n3.n
print(n1.n)



