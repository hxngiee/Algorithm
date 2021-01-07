# 부모 클래스가 갖는 모든 메소드가 자식 클래스에도 담긴다
# 자식 클래스에는 별도의 메소드를 추가할 수 있다.
# 한 번에 둘 이상의 클래스를 상속하는 것도 가능하다

class Father:
    def run(self):
        print("so fast!!")
class Mother:
    def dive(self):
        print("so deep!!")
class Son(Father, Mother):
    def jump(self):
        print("so high!!")

def main():
    s = Son()   # 아들 객체를 생성하여 s에 담음
    s.run()
    s.dive()
    s.jump()

main()

## 메소드 오버라이딩과 super
# 메소드 오버라이딩 : 상속관계에 있어 부모 클래스가 갖는 메소드와 동일한 이름의 메소드를 자식 클래스가 정의하는 경우
# class Father:
#     def run(self):
#         print("so fast,, dad style")
# class Son(Father):
#     def run(self):
#         print("so fast,, son style")
#     def run2(self):
#         super().run()
# def main():
#     s = Son()
#     s.run() # Son의 run 메소드가 호출됨
#     s.run2() # 부모 클래스의 run 호출 방법, 가려진 run 호출 방법

## __init__ 메소드의 오버라이딩
class Car:
    def __init__(self,id,f):
        self.id = id
        self.fuel = f
    def drive(self):
        self.fuel -= 10
    def add_fuel(self,f):
        self.fuel +=f
    def show_info(self):
        print("id:",self.id)
        print("fuel:",self.fuel)

# Car를 상속하는 Truck 클래스는 다음의 형태로 __init__ 메소드를 정의해야 Truck에 속한 변수 뿐만아니라 Car에 속한 변수도 적절히 생성되고 최기화 된다
# Truck은 Car를 상속하는데 Car의 멤버인 id와 fuel를 적절히 초기화 시킬 의무를 가짐(부모 class의 초기화를 위한 인자를 받아도됨 -> id,f)
class Truck(Car):
    def __init__(self,id,f,c):
        super().__init__(id,f)
        self.cargo = c
    def add_cargo(self,c):
        self.cargo += c
    def show_info(self):
        super().show_info()
        print("cargo:",self.cargo)

def main():
    t = Truck("42럭 2412", 0, 0)
    t.add_fuel(100)
    t.add_cargo(50)
    t.drive()
    t.show_info()
main()
