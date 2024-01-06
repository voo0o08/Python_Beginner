'''
ch29
'''

# 29.7 연습문제: 몫과 나머지를 구하는 함수 만들기
x = 10; y = 3
def get_quotient_remainder(n1, n2):
    return n1//n2, n1%n2
quotient, remainder = get_quotient_remainder(x,y)
print("몫: {0}, 나머지: {1}".format(quotient, remainder))

# 29.8 심사문제: 사칙 연산 함수 만들기
'''
숫자 두개 공백 입력
사칙 연산 결과 출력
'''
# x, y = map(int, input().split())
# def calc(n1, n2):
#     return n1+n2, n1-n2, n1*n2, n1/n2
# a, s, m, d = calc(x, y)
# print("덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}".format(a, s, m, d))

'''
ch30 함수에서 위치 인수와 키워드 인수 사용하기
'''
# def print_numbers(a, b, c):
#     print(a, b, c)
# x = [3, 6, 0]
# print_numbers(*x)

# 30.6 연습문제: 가장 높은 점수를 구하는 함수 만들기
korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*sub):
    return max(sub)

max_score = get_max_score(korean, english, mathematics, science)
print("높은 점수: ", max_score)

max_score = get_max_score(english, science)
print("높은 점수: ", max_score)

# 30.7 심사문제: 가장 낮은 점수, 높은 점수, 평균 점수를 구하는 함수 만들기
korean, english, mathematics, science = map(int, input().split())
def get_min_max_score(*subs):
    return min(subs), max(subs)

def get_average(**subDict):
    return sum(subDict.values())/len(subDict)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
