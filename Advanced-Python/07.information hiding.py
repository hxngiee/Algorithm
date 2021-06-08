## 객체 외부에서 객체 내에 있는 변수(속성)에 직접 접근하지 못하도록 하는 것
# _변수(경고: 바꾸려면 바꿀 수 있음) / __변수(차단)

class Person:
    def __init__(self,n,a):
        # self._name = n    # 관례적으로 _을 하나 쓰기도 하는데
        # self._age = n     # 똑같이 해당 변수에 직접 접근하지 말라는 것
        self.__name = n     # __두개 붙이면 외부에서 직접접근 못하도록함
        self.__age = a      # 클래스 객체 내에서만 접근 가능!
    def add_age(self,a):
        if (a<0):
            print('나이 정보 오류')
        else:
            self.__age += a
    def __str__(self):
        return '{0}: {1}'.format(self.__name,self.__age)

p = Person('James',22)
# p.__age += 1  # 이 문장 실행하면 오류 발생
# p._age +=1    # 이렇게 안쓰기로 했다
p.add_age(1)
print(p)


## __dict___ 변수
# 객체의 변수 정보(속성 정보)를 담고 있는 딕셔너리
# __dict__을 보면 객체 내 어떤 변수값을 가졌는지 알 수 있다
class Person:
    def __init__(self,n,a):
        self._name = n
        self._age = a
p = Person('James', 22)
print(p.__dict__)   #  객체 내에 있는 딕셔너리 정보 출력
# __dict__ 멤버는 class당 1개가 아닌 객체당 1개씩을 가지게 됨

