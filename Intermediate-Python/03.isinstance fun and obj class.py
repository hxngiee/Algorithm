class Fruit:
    pass

class Apple(Fruit):
    pass

class SuperApple(Apple):
    pass

sa = SuperApple()

print(isinstance(sa, Apple))
print(isinstance(sa,Fruit))

## object class
# 파이썬의 모든 클래스는 object 클래스를 직접 혹은 간접 상속한다

class Simple:
    pass

print(isinstance(Simple(),object))
print(isinstance([1,2],object))

class A:
    pass

class Z(A):
    pass

print(issubclass(Z,A))
print(issubclass(type,object))






