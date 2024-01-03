'''
실습
- 문자열 여러 개와 실수 여러 개를 입력 받기 => input() 1개만 사용
- 첫번째 입력 받은 값은 Key
- 두번째 입력 받은 값은 value
- 딕셔너리로 저장해 주세요
'''
data = input("문자열과 실수 여러 개 입력\n단, 문자열과 실수 개수 동일(예:aa bb cc, 1.1 2.2 3.3)")
# 입력 형식이 맞을 경우만 딕셔너리에 저장
# - 입력 "   ,   " 문자열 안에 ',' 존재해야 함
# - 문자열과 실수 개수가 동일해야함
if ',' in data: # T/F
    dataList = data.split(',') # dataList = ["aa bb cc", "1.1 2.2 3.3"]
    key = dataList[0].split()
    value = dataList[1].split()
else:
    print("정확한 형식이 아닙니다.")