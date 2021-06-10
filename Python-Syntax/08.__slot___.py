## 딕셔너리는 튜플, 리스트에 비해 메모리 사용량이 많음(key값으로 value를 얻을 수 있도록 더 많은 정보를 유지하기 때문)
# 이는 수천 개에 이르는 딕셔너리 생성시 시스템에 부담을 줌
class Point3D:
    __slots__ = ('x','y','z')       # 이 클래스를 기반으로 생성된 객체의 변수는 x,y,z로 제한한다 !
                                    # 이 객체는 x,y,z에 direct하게 접근 하도록 함! dict을 통해 하는 것이 아닌

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({0}, {1}, {2})'.format(self.x,self.y,self.z)

p1 = Point3D(1,1,1)
p2 = Point3D(24,15,71)
print(p1)
print(p2)

# p1.w = 30     # 즉, x,y,z 이외에 다음과 같이 객체에 변수를 추가하는 것이 불가능이 됨
# 이렇게 __slots__을 통해 변수의 수와 이름을 제한하면 객체별로 __dict__이 생기지 않음. 클래스당 하나의 __slots__만 생성되 메모리상 큰 이득

