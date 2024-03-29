'''
function
- 특정 기능을 구현 하기 위한 코드 묶음을 의미
- 자주 사용되는 기능을 함수로 구현함
return : 리턴값/반환값/결과값
매개 변수 : 파라미터
def 함수명(매개변수1, 매개변수2, ... 매개변수n):
    실행코드
    실행코드
    return 결과
함수 사용 => 함수 호출 (calling)
방법 : 함수이름(데이터, 데이터 ... )
'''
# 함수 기능 : 2개의 숫자의 합계를 계산 후 결과를 반환 해주는 기능
# 함수 이름 : addTwo
# 매개 변수 : x, y
# 반 환 값 : 합계

def addTwo(x, y):
    value = x+y
    return value

print(addTwo(11, 2))

# 함수 기능 : 2개의 숫자의 곱셈 결과를 계산 후 결과를 반환 해주는 기능
# 함수 이름 : mulTwo
# 매개 변수 : x, y
# 반 환 값 : 곱셈 결과

def mulTwo(x, y):
    val = x * y
    return val

print(mulTwo(11, 9))




