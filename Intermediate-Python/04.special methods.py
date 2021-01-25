## Special Methods
# 프로그래머가 이름을 직접 명시하여, 직접 그 이름을 명시하지 않고 다른 경로를 통해서 자동으로 호출되는 메소드, 호출시점이 약속된 메소드.
# __name__

# t = (1,2,3)
# len(t)  # t.__len__()
#
# itr = iter(t)   # itr = t.__iter__()
# for i in itr:
#     print(i, end=' ')
#
# s = str(t)  # t.__str__()


## 예제
class Car:
    def __init__(self, id):
        self.id = id
    def __len__(self):
        return len(self.id)
    def __str__(self):
        return 'Vehicle number : ' + self.id

c = Car("32러5234")
print(len(c))   # __len__ 메소드가 호출됨
print(str(c))   # __str__ 메소드가 호출됨

## iterable, iterator 객체 만들기
# iterable 객체 : iter 함수에 인자로 전달 가능한 객체, 그 결과로 'iterator'객체 반환
# 조건 : 스폐셜 메소드인 __iter__가 존재해야 한다

# iterator 객체 : next 함수에 인자로 전달 가능한 객체
# 조건 : 스폐셜 메소드인 __next__가 존재해야 한다

class Car:
    def __init__(self,id):
        self.id = id
    def __iter__(self):         # 스폐셜 메소드
        return iter(self.id)    # 변수 id의 iterator 객체를 반환
                                # Car 객체가 iterable 객체가 되도록 함

c = Car("32러5234")
for i in c:                      # Car 객체가 iterable 객체라는 증거 !
    print(i, end=' ')


# iterator 객체가 되게끔 하기
# __next__ 메소드 next함수 호출 시 불리는 스폐셜 메소드
    # 조건 1. 가지고 있는 값을 하나씩 반환
    # 조건 2. 더 이상 반환 값이 없을 경우 StopIteration 예외 발생

class Coll:
    def __init__(self,d):
        self.ds = d     # 인자로 전달된 값을 저장(밑에 예제의 경우 list)
        self.cc = 0
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc - 1]

co = Coll([1,2,3,4,5])
while True:
    try:
        i = next(co)
        print(i, end=' ')
    except StopIteration:
        break

# 위의 예제의 경우 Coll 클래스 객체는 iter 함수 호출이 아닌 튜플 및 문자열로 전달되었으나 그래도 이는 iterator 객체에 해당 됨
# next 함수의 인자로 전달이 되어 저장된 값을 하나씩 반환할 뿐 아니라 더 이상 반환할 값이 없으면 StopIteration 예외도 발생시키기 때문

## 예제 확장 - iterable 객체를 인자로 전달하면서 iter 함수를 호출하여 iterator 객체 반환하기

class Coll2:
    def __init__(self,d):
        self.ds = d
    def __next__(self):
        if len(self.ds) <= self.cc:
            raise StopIteration
        self.cc += 1
        return self.ds[self.cc - 1]
    def __iter__(self):
        self.cc = 0     # next 호출 횟수 초기화
        return self     # 이 객체(iterator처럼 동작,, __next__가 있기 때문)를 그대로 반환함

co = Coll2([1,2,3,4,5])
for i in co:    # for 루프 진행 과정에서 iter 함수 호출됨
    print(i, end=' ')

for i in co:    # for 루프 진행 과정에서 iter 함수 호출됨
    print(i, end=' ')

co = Coll2('hello')
itr = iter(co)
print(itr is co)   # itr과 co는 동일한 객체인가?? -> True
