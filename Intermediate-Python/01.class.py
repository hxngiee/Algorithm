## 객체 안에 변수가 만들어지느 시점
class Simple:
    def seti(self,i):
        self.i = i
    def geti(self):
        return self.i

s1 = Simple()
s1.seti(200) # 이 메소드의 실행 과정에서 객체 내 변수 i가 만들어진다
print(s1.geti())

## 객체에 변수와 메소드를 붙였다 뗴었다 해보기
class SoSimple:
    def geti(self):
        return self.i

ss = SoSimple()
ss.i = 27   # 이 순간 변수 ss에 담긴 객체에 i라는 변수가 생김
print(ss.geti())    ##ss에 담긴 객체에 i가 생겼으므로 geti 메소드 호출 가능

ss.hello = lambda : print('hi~~')   # hello라는 메소드 추가(객체에 함수를 추가할 수 있다))
ss.hello()

del ss.i        # ss에 담긴 객체에서 변수 i 삭제
del ss.hello    # ss에 담긴 객체에서 메소도 hello 삭제

## 클레스에 변수 추가하기
# 파이썬의 클래스는 클래스이자 객체이다
class Simple:
    def __init__(self,i):
        self.i = i
    def geti(self):
        return self.i

Simple.n = 7
print(Simple.n)

s1 = Simple(3)
s2 = Simple(5)

print(s1.n, s1.geti(), sep = ', ')
print(s2.n, s2.geti(), sep = ', ')
# 클레스에 속하는 변수를 만들 수 있다. 객체에 찾는 변수가 없으면 해당 객체의 클래스로 찾아가서 그 변수를 찾는다

print(type)
print(type([1,2]))
print(type(list))

class Simple:
    pass
print(type(Simple))
