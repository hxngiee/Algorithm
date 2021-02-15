# 파이썬의 함수는 객체이기 때문에 반환 가능하다 다른 함수를 호출할 때 인자로도 전달이 가능


def maker(m):
    def inner(n):      # 함수 안에서 정의된 함수, nested 함수라 한다
        return m*n
    return inner       # 위에서 정의한 nested 함수 반환

# closure : 안쪽에 위치한 nested 함수가 자신이 필요한 변수의 값을 어딘가에 저장해 놓고 쓰는 테크닉
# nested 함수가 필요한 변수(m)을 어딘가에 저장해 놓는 기술

f1 = maker(2)
f2 = maker(3)

print(f1.__closure__[0].cell_contents)
print(f2.__closure__[0].cell_contents)