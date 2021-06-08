## 연산자(+, -, ^, /)가 가지고 있는 기본적인 기능 및 결과를 유지하는 형태로 오보로딩 해야한다
# 내부적으로 곱셈과 관련된 일을 하고 또 그 `결과`를 반환하도록 오버로딩 해야함

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    def __call__(self):
        return 'Vector({0},{1})'.format(self.x,self.y)

v1 = Vector(3,3)
v2 = Vector(7,7)
v3 = v1 + v2
print(v1())
print(v2())
print(v3())

## 메소드 __str__의 정의
# 객체가 갖는 정보를 단순 확인
class Simple:
    def __init__(self,i):
        self.i = i

s = Simple(10)

print(s)    # s.__strs__()을 출력하는 것과 같다
print(s.__str__())

## 위 정보는 보편적으로 필요하지 않음.
# 아래와 같이 메소드를 오버라이딩 하는 것이 바람직
class Simple:
    def __init__(self,i):
        self.i = i
    def __str__(self):
        return 'Simple({0})'.format(self.i)

s = Simple(10)

print(s)

## 단순 정보 확인이 목적일땐 __call___보단 __str___ 메소드를 오버로딩 하는 것이 더 좋다
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    def __call__(self):
        return 'Vector({0},{1})'.format(self.x,self.y)
    def __str__(self):
        return 'Vector({0}, {1})'.format(self.x,self.y)

v1 = Vector(3,3)
v2 = Vector(7,7)
v3 = v1 + v2

print(v1)
# print(v1())   # 메소드를 str로 오보로딩 해줬기 때문에 ()을 쓸 필요가 없어짐

print(v2)
# print(v2())

print(v3)
# print(v3())
